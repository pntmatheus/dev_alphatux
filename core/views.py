import os

import re

from django.http import HttpResponse

from .models import Pessoa

from openpyxl import load_workbook
import paramiko

"""
def index(request):
    return HttpResponse("Olá Mundo!!!")
"""
## Achei interessante separar em duas funções para melhor trabalhar no "find" do Mikrotik
def gera_codigo_comentario(id):
    return "##%s##" % id

def faz_cometario(nome, id):
    return "\"%s --- %s\"" % (gera_codigo_comentario(id), nome)


'''
it accepts 12 hex digits with either : or - as separators between pairs (but the separator must be uniform... either all separators are : or are all -).

This is the explanation:

    ## [0-9a-f] means an hexadecimal digit
    ## {2} means that we want two of them
    ## [-:] means either a dash or a colon. Note that the dash as first char doesn't mean a range but only means itself. This atom is enclosed in parenthesis so it can be reused later as a back reference.
    ## [0-9a-f]{2} is another pair of hexadecimal digits
    ## \\1 this means that we want to match the same expression that we matched \"before as separator. This is what guarantees uniformity. Note that the regexp syntax is \1 but I'm using a regular string so backslash must be escaped by doubling it.
    ## [0-9a-f]{2} another pair of hex digits
    ## {4} the previous parenthesized block must be repeated exactly 4 times, giving a total of 6 pairs of digits: <pair> <sep> <pair> ( <same-sep> <pair> ) * 4
    ## $ The string must end right after them

'''
def valida_mac(mac):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        mac = mac.upper()
        return mac
    else:
        return "FALHOU PQ O %s NAO EH UM MAC VALIDO!!!!" % mac


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
            retorno.append("OK! ---------->" + comando + " <br>")

    return retorno

'''
def valida_comando(ssh_session, comandos):

    retorno = ""
    mikrotik = ""
    for comando in comandos:
        mikrotik = mikrotik + "%s;" % (comando)
        retorno = mikrotik

    ssh_session.exec_command(mikrotik)

    return retorno '''

def add_plano(nome, download, upload, comandos):

    plano = "/ip hotspot user profile add idle-timeout=none name=%s rate-limit=%s/%s shared-users=1 status-autorefresh=1m transparent-proxy=no add-mac-cookie=no" % (nome,upload,download)
    plano_bloqueado = "/ip hotspot user profile add advertise=yes advertise-interval=0s advertise-timeout=immediately advertise-url=bloqueado.html idle-timeout=none name=bloqueado-%s open-status-page=always shared-users=1 status-autorefresh=1m transparent-proxy=yes add-mac-cookie=no" % (nome)
    comandos.append(plano)
    comandos.append(plano_bloqueado)
    return comandos

def add_ip_gateway(nome, ip, id):
    comment = faz_cometario(nome, id)
    comando = "ip address add address=%s interface=bridge-clientes comment=%s" % (ip, comment)
    return comando

def add_dhcp_network(nome, ip_rede, ip_gateway, ip_dns, id):
    comment = faz_cometario(nome, id)
    comando = "ip dhcp-server network add address=%s comment=%s dns-server=%s gateway=%s" % (ip_rede, comment, ip_dns, ip_gateway)
    return comando

def add_dhcp_lease(nome, ip_cliente, mac, id):
    comment = faz_cometario(nome, id)
    comando = "ip dhcp-server lease add address=%s comment=%s mac-address=%s" % (ip_cliente, comment, mac)
    return comando

def add_hotspot_user(nome, mac, plano, id):
    comment = faz_cometario(nome, id)
    comando = "/ip hotspot user add comment=%s mac-address=%s name=%s profile=%s" % (comment, mac, mac, plano)
    return comando

def add_hotspot_ip_binding(nome, ip_cliente, mac, comandos, id):
    comment = faz_cometario(nome, id)
    comandos.append("/ip hotspot ip-binding add address=%s comment=%s mac-address=%s type=regular" % (ip_cliente, comment, mac))
    comandos.append("/ip hotspot ip-binding move destination=[find comment=\"BLOQUEAR RESTANTE\"] numbers=[find comment=%s];" % comment)
    return comandos


## ALTERA O IP NO /IP ADDRESS - INFORMAR ***SEMPRE*** IP+MASCARA (/30, /24, ...)
def altera_ip_ip_address(id, ip):
    comando = "/ip address set [/ip address find comment~\"%s\"] address=%s" % (gera_codigo_comentario(id), ip)
    return comando
## ALTERA O NOME DO CLIENTE NO COMENTARIO DO IP ADDRESS
def altera_nome_ip_address(id, nome):
    comando = "/ip address set [/ip address find comment~\"%s\"] comment=%s" % (gera_codigo_comentario(id), faz_cometario(nome, id))
    return comando

## ALTERA OS IPS DE REDE E GATEWAY DO DHCP NETWORKS, PRECISA SER MELHORA A QUESTAO DE VALIDAR OS IPS
###IP DA REDE DEVE SER ACOMPANHADO PELO BIT DE MASCARA
def altera_ip_dhcp_networks(id, ip_rede, ip_gateway):
    comando = "/ip dhcp-server network set [find comment~\"%s\"] address=%s gateway=%s" % (gera_codigo_comentario(id), ip_rede, ip_gateway)
    return comando

def altera_nome_dhcp_networks(id, nome):
    comando = "/ip dhcp-server network set [find comment~\"%s\"] comment=%s;" % (gera_codigo_comentario(id), faz_cometario(nome, id))
    return comando

def altera_ip_dhcp_lease(id, ip):
    comando = "/ip dhcp-server lease set [find comment~\"%s\"] address=%s" % (gera_codigo_comentario(id), ip)
    return comando

def altera_mac_dhcp_lease(id, mac):
    comando = "/ip dhcp-server lease set [find comment~\"%s\"] mac-address=\"%s\"" % (gera_codigo_comentario(id), mac)
    return comando

def altera_nome_dhcp_lease(id, nome):
    comando = "/ip dhcp-server lease set [find comment~\"%s\"] comment=%s;" % (gera_codigo_comentario(id), faz_cometario(nome, id))
    return comando

def altera_mac_hotspot_user(id, mac):
    comando = "/ip hotspot user set [find comment~\"%s\"] name=\"%s\" mac-address=\"%s\"" % (gera_codigo_comentario(id), mac, mac)
    return comando

def altera_profile_hotspot_user(id, profile):
    comando = "/ip hotspot user set [find comment~\"%s\"] profile=\"%s\"" % (gera_codigo_comentario(id), profile)
    return comando

def altera_nome_hotspot_user(id, nome):
    comando = "/ip hotspot user set [find comment~\"%s\"] comment=%s;" % (gera_codigo_comentario(id), faz_cometario(nome, id))
    return comando

def altera_ip_hotspot_bindings(id, ip):
    comando = "/ip hotspot ip-binding set [find comment~\"%s\"] address=%s" % (gera_codigo_comentario(id), ip)
    return comando

def busca_existencia(comando):
    verifica = ":if ([:len [%s]] > 0) do={:put \"Found\";} else={:put \"Not Found\";};" % comando
    return verifica

def index(request):



    path = os.path.join(os.environ['HOME'], '.ssh', 'id_dsa')
    pkey = paramiko.DSSKey.from_private_key_file(path, password=None)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.13', username='admin', pkey=pkey)

    backup = False
    comandos = []

    if (backup):
        #CONFIGURACOES INICIAIS
        wb = load_workbook(filename='clientesTerezinha.xlsx', read_only=True)
        ws = wb['Plan1']

        clientes = []
        macs = []
        ids = []

        for p in ws["A1":"C76"]:
            ids.append(p[0].value)
            clientes.append(p[1].value)
            macs.append(p[2].value)


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
        for (nome_cliente,mac, id_cliente) in zip(clientes,macs, ids):
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
            comandos.append(add_ip_gateway(nome_cliente,ip_gateway+mascara, id_cliente))
            ###Adicionar DHCP Networks
            comandos.append(add_dhcp_network(nome_cliente, ip_rede, ip_gateway, ip_dns, id_cliente))
            ###Adicionar DHCP Lease
            comandos.append(add_dhcp_lease(nome_cliente, ip_cliente, mac, id_cliente))
            ###Adicionar HOTSPOT USER
            comandos.append(add_hotspot_user(nome_cliente, mac, "1M", id_cliente))
            ###Adicionar HOTSPOT IP BINDING
            comandos = add_hotspot_ip_binding(nome_cliente, ip_cliente, mac, comandos, id_cliente)
            contador += 1

        ##ADD HOTSPOT --- COLOQUEI AQUI PQ LOGO QUE SE CRIA O HOTSPOT O MIKROTIK BLOQUEIA AS ENTRADAS PELO FIREWALL
        comandos.append("/ip hotspot ip-binding add address=192.168.1.11 type=bypassed comment=\"ServidorDjango\"")
        comandos.append("/ip hotspot ip-binding move destination=0 numbers=[find comment~\"ServidorDjango\"];")
        ##Adicionar HOTSPOT
        comandos.append("/ip hotspot add disabled=no idle-timeout=none interface=bridge-clientes keepalive-timeout=none name=Alphatux profile=alphatux-z3")


    teste = True

    if(teste):
        mamae = 0
        #tt#ALTERAR CLIENTES
        #comandos.append(":if ([:len [:find \"abcd\" \"x\"]] > 0) do={:put \"Found\";} else={:put \"Not Found\";};")
        ##teste altera_ip_ip_address
        #comandos.append(altera_ip_ip_address(4, "192.168.23.5/24"))
        ##teste altera_nome_ip_address
        #comandos.append(altera_nome_ip_address(4, "Testando..."))
        ##teste altera_ip_dhcp_networks
        #comandos.append(altera_ip_dhcp_networks(5, "192.168.25.8/30", "192.168.25.9"))
        #teste altera_nome_dhcp_networks
        #comandos.append(altera_nome_dhcp_networks(75, "Matheus2"))
        #teste altera_ip_dhcp_lease
        #comandos.append(altera_ip_dhcp_lease(5, "192.168.24.6"))
        #teste altera_ip_dhcp_lease
        #comandos.append(altera_mac_dhcp_lease(6, valida_mac("00:0c:29:de:a3:7a")))
        #teste altera_nome_dhcp_lease
        #comandos.append(altera_nome_dhcp_lease(7, "Matheus Testado..."))
        #teste altera_mac_hotspot_user
        #comandos.append(altera_mac_hotspot_user(4, valida_mac("00:0c:29:de:a3:7a")))
        #teste altera_profile_hotspot_user
        #comandos.append(altera_profile_hotspot_user(9, "2M"))
        #teste altera_nome_hotspot_user
        #comandos.append(altera_nome_hotspot_user(5, "Amanda Teste"))
        #teste altera_ip_hotspot_binding
        comandos.append(altera_ip_hotspot_bindings(7, "192.168.26.6"))


    resultado = valida_comando(ssh, comandos)






    return HttpResponse(resultado)

    ssh.close()