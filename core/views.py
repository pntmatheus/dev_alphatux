import os

from django.http import HttpResponse

from .models import Pessoa

from openpyxl import load_workbook
import paramiko

"""
def index(request):
    return HttpResponse("Olá Mundo!!!")
"""

def index(request):

    wb = load_workbook(filename='clientesTerezinha.xlsx', read_only=True)
    ws = wb['Plan1']

    clientes = []
    macs = []

    for p in ws["A1":"B78"]:
        clientes.append(p[0].value)
        macs.append(p[1].value)

    path = os.path.join(os.environ['HOME'], '.ssh', 'id_dsa')
    pkey = paramiko.DSSKey.from_private_key_file(path, password=None)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.13', username='teste', pkey=pkey)

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

    stdin,stdout,stderr = ssh.exec_command('ip address print')
    output = '<br>'.join([p for p in stdout])

    #output = stderr.read()
    #output = stdout.readlines()

    return HttpResponse(comando)