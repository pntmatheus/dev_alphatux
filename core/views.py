import os

from django.http import HttpResponse

from .models import Pessoa

from openpyxl import load_workbook
import paramiko

"""
def index(request):
    return HttpResponse("Olá Mundo!!!")
"""

def valida_comando(ssh_session, comandos):

    retorno = []
    for comando in comandos:
        mikrotik = ":do { :put [%s];} on-error={ :put \"deu merda\"; }" % comando
        stdin, stdout,stderr = ssh_session.exec_command(mikrotik)
        if any("deu merda" in s for s in stdout):
            stdin, stdout,stderr = ssh_session.exec_command(comando)
            teste = stdout.read()
            teste = teste.decode("utf-8")
            retorno.append("FALHOU!!!!     ----------->     " + comando + " ----->> " + teste + "<br>")
            #status = "FALHOU!!!!     ----------->     " + comando + " ----->> " + teste

        #teste = "\n".join(item for item in stdout.read().splitlines() if '>' not in item)
        else:
            #status = "Deu tudo certo"
            status = stdout.read()
            status = status.decode("utf-8")
            retorno.append("OK! ---------->" + comando + " ----> " + status + " <br>")
    return retorno

def add_plano(nome, download, upload, comandos):

    plano = "/ip hotspot user profile add idle-timeout=none name=%s rate-limit=%s/%s shared-users=1 status-autorefresh=1m transparent-proxy=no add-mac-cookie=no" % (nome,upload,download)
    plano_bloqueado = "/ip hotspot user profile add advertise=yes advertise-interval=0s advertise-timeout=immediately advertise-url=bloqueado.html idle-timeout=none name=bloqueado-%s open-status-page=always shared-users=1 status-autorefresh=1m transparent-proxy=yes add-mac-cookie=no" % (nome)
    comandos.append(plano)
    comandos.append(plano_bloqueado)
    return comandos

def add_ip_gateway(nome, ip):
    nome = "\"%s\"" % nome
    comando = "ip address add address=%s interface=bridge-clientes comment=%s" % (ip, nome)
    return comando

def add_dhcp_network(nome, ip_rede, ip_gateway, ip_dns):
    nome = "\"%s\"" % nome
    comando = "ip dhcp-server network add address=%s comment=%s dns-server=%s gateway=%s" % (ip_rede, nome, ip_dns, ip_gateway)
    return comando

def add_dhcp_lease(nome, ip_cliente, mac):
    nome = "\"%s\"" % nome
    comando = "ip dhcp-server lease add address=%s comment=%s mac-address=%s" % (ip_cliente, nome, mac)
    return comando

def add_hotspot_user(nome, mac, plano):
    nome = "\"%s\"" % nome
    comando = "/ip hotspot user add comment=%s mac-address=%s name=%s profile=%s" % (nome, mac, mac, plano)
    return comando

def add_hotspot_ip_binding(nome, ip_cliente, mac, comandos):
    nome = "\"%s\"" % nome
    comandos.append("/ip hotspot ip-binding add address=%s comment=%s mac-address=%s type=regular" % (ip_cliente, nome, mac))
    comandos.append("/ip hotspot ip-binding move destination=[find comment=\"BLOQUEAR RESTANTE\"] numbers=[find comment=%s];" % nome)
    return comandos

def busca_existencia(comando):
    verifica = ":if ([:len [%s]] > 0) do={:put \"Found\";} else={:put \"Not Found\";};" % comando
    return verifica

def altera_ip_ip_address(nome, ip_novo, mascara, comandos):
    nome = "\"%s\"" % nome

    comando = "/ip address set [/ip address find comment~%s] address=%s network=%s" % (nome, ip_novo, mascara)
    return comando


def index(request):



    path = os.path.join(os.environ['HOME'], '.ssh', 'id_dsa')
    pkey = paramiko.DSSKey.from_private_key_file(path, password=None)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.13', username='admin', pkey=pkey)

    backup = 0
    comandos = []

    if backup == 1:
        #CONFIGURACOES INICIAIS
        wb = load_workbook(filename='clientesTerezinha.xlsx', read_only=True)
        ws = wb['Plan1']

        clientes = []
        macs = []

        for p in ws["A1":"B76"]:
            clientes.append(p[0].value)
            macs.append(p[1].value)

        ##Criar BRIDGE CLIENTES
        comandos.append("/interface bridge add comment=\"Bridge dos Clientes\" name=bridge-clientes admin-mac=[/interface get ether1 mac-address] auto-mac=no")
        ##SETAR IP NA BRIDGE
        comandos.append("/ip address add address=192.168.10.1/24 comment=\"IP Inicial da BRIDGE CLIENTES\" interface=bridge-clientes")
        ##Adicionar INTERFACE 1 NA BRIDGE
        comandos.append("/interface bridge port add bridge=bridge-clientes interface=ether1")
        ##Criar DHCP SERVER
        comandos.append("/ip dhcp-server add add-arp=yes lease-time=3d address-pool=static-only interface=bridge-clientes name=\"AlphatuxZ3\" disabled=no")
        ##Adicionar PROFILE HOTSPOT
        comandos.append("/ip hotspot profile add dns-name=\"\" hotspot-address=0.0.0.0 html-directory=hotspot http-proxy=0.0.0.0:0 login-by=mac mac-auth-password=\"\" name=alphatux-z3 rate-limit=\"\" smtp-server=0.0.0.0 use-radius=no")
        ##Adicionar Planos no HOTSPOT USER PROFILE
        ###Basico
        comandos = add_plano("basico","256k","156k",comandos)
        ###Intermediario
        comandos = add_plano("intermediario","500k","300k",comandos)
        ###1M
        comandos = add_plano("1M", "1000k", "400k", comandos)
        ###2M
        comandos = add_plano("2M", "2000k", "400k", comandos)
        ###Matheus
        comandos = add_plano("matheus", "14500k", "2500k", comandos)
        ###Ultra
        comandos = add_plano("ultra", "3000k", "100k", comandos)
        ##Adicionar REGRA IP BINDING
        comandos.append("/ip hotspot ip-binding add address=0.0.0.0/0 comment=\"BLOQUEAR RESTANTE\" type=blocked")


        #ADD CLIENTES
        sufixo = "192.168"
        contador = 20
        rede = 0
        gateway = 1
        cliente = 2
        mascara = "/30"
        for (c,m) in zip(clientes,macs):
            if contador > 200:
                contador = 20
                gateway += 4
                rede += 4
                cliente += 4

            ip_gateway =  "%s.%s.%s" % (sufixo,str(contador),str(gateway))
            ip_rede = "%s.%s.%s%s" % (sufixo, str(contador), str(rede), mascara)
            ip_dns = "192.168.2.1"
            ip_cliente = "%s.%s.%s" % (sufixo, str(contador), str(cliente))

            ###Adicionar IPS GATEWAY-CLIENTE
            comandos.append(add_ip_gateway(c,ip_gateway+mascara))
            ###Adicionar DHCP Networks
            comandos.append(add_dhcp_network(c, ip_rede, ip_gateway, ip_dns))
            ###Adicionar DHCP Lease
            comandos.append(add_dhcp_lease(c, ip_cliente, m))
            ###Adicionar HOTSPOT USER
            comandos.append(add_hotspot_user(c, m, "1M"))
            ###Adicionar HOTSPOT IP BINDING
            comandos = add_hotspot_ip_binding(c, ip_cliente, m, comandos)
            contador += 1

    ##ALTERAR CLIENTES
    comandos.append(":if ([:len [:find \"abcd\" \"x\"]] > 0) do={:put \"Found\";} else={:put \"Not Found\";};")
    comandos.append(altera_ip_ip_address("#25776#", "192.168.20.5", "255.255.255.252"))



    teste = valida_comando(ssh, comandos)






    return HttpResponse(teste)

    ssh.close()
"""
    #### IP ADDRESS
    contador = 5
    for t in clientes:

        comando = "ip address add address=192.168." + str(contador) + ".1/30 interface=ether1 comment=" + t
        ssh.exec_command(comando)
        contador = contador + 1

    #### IP DHCP NETWORKS
    contador = 5
    for (c,m) in zip(clientes,macs):

        comando = "ip dhcp-server network add address=192.168."+str(contador)+".0/30 comment="+c+" dns-server=192.168.2.1 gateway=192.168."+str(contador)+".1"
        ssh.exec_command(comando)
        contador = contador + 1

    #### IP DHCP LEASES

    contador = 5
    for (c,m) in zip(clientes,macs):

        comando = "ip dhcp-server lease add address=192.168."+str(contador)+".2 comment="+c+" mac-address="+m
        ssh.exec_command(comando)
        contador = contador + 1

    #### HOTSPOT USERS

    contador = 5
    for (c,m) in zip(clientes,macs):

        comando = "ip hotspot user add comment="+c+" mac-address="+m+" name="+m
        ssh.exec_command(comando)
        contador = contador + 1

    #### IP BINDINGS
    contador = 5
    for (c,m) in zip(clientes,macs):

        comando = "ip hotspot ip-binding add address=192.168."+str(contador)+".2 comment="+c+" mac-address="+m
        ssh.exec_command(comando)
        contador = contador + 1
"""
