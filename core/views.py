from django.http import HttpResponse

from .models import Pessoa

"""
def index(request):
    return HttpResponse("Olá Mundo!!!")
"""

def index(request):
    teste = Pessoa.objects.all()
    output = ', '.join([p.nome for p in teste])
    return HttpResponse(output)