import os

from django.http import HttpResponse

from .models import Pessoa

import paramiko

"""
def index(request):
    return HttpResponse("Olá Mundo!!!")
"""

def index(request):

    path = os.path.join(os.environ['HOME'], '.ssh', 'id_dsa')
    pkey = paramiko.DSSKey.from_private_key_file(path, password=None)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.13', username='admin-ssh', pkey=pkey)

    stdin,stdout,stderr = ssh.exec_command('ip address print')

    output = '<br>'.join([p for p in stdout])

    #output = stderr.read()
    #output = stdout.readlines()
    return HttpResponse(output)