from django.http import HttpResponse

from .models import Pessoa

import paramiko

"""
def index(request):
    return HttpResponse("Olá Mundo!!!")
"""

def index(request):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.13', username='admin', password='admin')

    stdin,stdout,stderr = ssh.exec_command('ip address print')

    teste = Pessoa.objects.all()
    #output = ', '.join([p.nome for p in teste])

    output = '<br>'.join([p for p in stdout])

    #output = stderr.read()
    #output = stdout.readlines()
    return HttpResponse(output)