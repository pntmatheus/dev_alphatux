# -*- coding: utf-8 -*-
from django.contrib import admin

from core.models import User, Recibo, Pessoa, TipoPolaridade, TipoPessoa, Pop, Cliente, DistribuidorInterno, AP, DispositivoCliente, Plano, Estado, Cidade, Bairro, TipoEndereco, Rua, Cep, Endereco, Equipamento, Fabricante
#from core.forms import DistribuirInternoForm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.conf import settings

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm

from pynum2word import dExtenso

from django.contrib import messages

from decimal import *

from django.utils.dateformat import format
from django.utils import formats

from django.template.defaultfilters import slugify

import re
import os

from django.http import HttpResponse

import datetime


def title_except(s):
   articles = ['e', 'an', 'of', 'the', 'is']
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in articles and word or word.capitalize())
   return " ".join(final)



def moeda_brasileira(numero):
    """
    Retorna uma string no formato de moeda brasileira
    """

    try:
        contador = 0
        preco_str = ''
        numero = Decimal(numero).quantize(Decimal('1.00'))
        num = numero.__str__()
        if '.' in num:
            preco, centavos = num.split('.')
        else:
            preco = num
            centavos = '00'

        tamanho = len(preco)
        while tamanho > 0:
            preco_str = preco_str + preco[tamanho-1]
            contador += 1
            if contador == 3 and tamanho > 1:
                    preco_str = preco_str + '.'
                    contador = 0
            tamanho -= 1

        tamanho = len(preco_str)
        str_preco = ''
        while tamanho > 0:
            str_preco = str_preco + preco_str[tamanho-1]
            tamanho -= 1

        return "R$ %s,%s" % (str_preco, centavos)
    except:
        return 'Erro. Nao foi possivel formatar.'




@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    pass

class EquipamentoInline(admin.StackedInline):
    model = Equipamento

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    inlines = [EquipamentoInline,]

@admin.register(TipoPessoa)
class TipoPessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoPolaridade)
class TipoPessoaAdmin(admin.ModelAdmin):
    pass


@admin.register(Pop)
class PopAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = list_display
    ordering = list_display
    list_filter = list_display
    

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome_cliente', 'apelido_cliente', 'cliente_desde')
    raw_id_fields = ('pessoa',)
    search_fields = ('pessoa__nome', 'id', 'pessoa__codigo', 'pessoa__nome_fantasia', 'pessoa__search_dump')

class ClienteInline(admin.StackedInline):
        model = Cliente

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codigo', 'nome_fantasia')
    list_display_links = list_display
    #ordering = list_display
    ordering = ['nome',]
    list_filter = ('nome',)
    search_fields = ('nome', 'id', 'codigo', 'nome_fantasia', 'search_dump')
    inlines = [ClienteInline,]
    raw_id_fields = ('endereco',)

    def save_model(self, request, obj, form, change):
        ### Gambiarra para procura com string sem acentuacao
        obj.search_dump = slugify(str(obj.nome + " " + obj.nome_fantasia))
        obj.save()



@admin.register(DistribuidorInterno)
class DistribuidorInternoAdmin(admin.ModelAdmin):


    list_display = ('get_cliente', 'equipamento', 'id', 'get_dono')
    list_display_links = list_display
    ordering = ['cliente__pessoa__nome',]
    list_filter = ('equipamento',)
    raw_id_fields = ('endereco', 'pessoa', 'cliente')



    def get_dono(self,obj):
        return obj.pessoa.nome

    def get_cliente(self,obj):
        return obj.cliente.pessoa.nome

    get_dono.short_description = 'Dono'
    get_cliente.short_description = 'Cliente'

@admin.register(AP)
class APAdmin(admin.ModelAdmin):
    list_display = ('ssid',)
    list_display_links = list_display
    ordering = list_display
    list_filter = ('ssid',)

@admin.register(DispositivoCliente)
class DispositivoClienteAdmin(admin.ModelAdmin):
    list_display = ('get_cliente', 'equipamento', 'get_dono')
    list_display_links = list_display
    ordering = ('equipamento',)
    list_filter = ('equipamento',)
    raw_id_fields = ('endereco', 'pessoa', 'cliente')

    def get_dono(self,obj):
        return obj.pessoa.nome

    def get_cliente(self,obj):
        return obj.cliente.pessoa.nome

    get_dono.short_description = 'Dono'
    get_cliente.short_description = 'Cliente'
    
@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')
    list_display_links = list_display
    ordering = list_display
    list_filter = ('nome',)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'abreviacao')
    list_display_links = list_display
    ordering = list_display
    list_filter = ('abreviacao',)


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    list_display_links = list_display
    ordering = list_display
    list_filter = ('nome',)

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    list_display_links = list_display
    ordering = list_display
    list_filter = ('nome',)

@admin.register(TipoEndereco)
class TipoEnderecoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'abreviacao')
    list_display_links = list_display
    ordering = list_display
    list_filter = ('abreviacao',)

@admin.register(Rua)
class RuaAdmin(admin.ModelAdmin):

    list_display = ('tipo_endereco','nome',)
    list_display_links = list_display
    ordering = list_display
    list_filter = ('tipo_endereco',)
    search_fields = ('nome',)

@admin.register(Cep)
class CepAdmin(admin.ModelAdmin):

    list_display = ('id','codigo', 'rua')
    list_display_links = list_display



@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    search_fields = ('estado__nome', 'cidade__nome', 'bairro__nome', 'rua__nome', 'numero')
    ordering = ['estado__nome', 'cidade__nome', 'bairro__nome', 'rua__nome', 'numero']



@admin.register(Recibo)
class ReciboAdmin(admin.ModelAdmin):
    #form = ReciboModelForm
    list_display = ('id', 'competencia', 'data_emissao', 'nome', 'valor_br', 'file_b', 'file_')
    list_display_links = list_display
    list_filter = ('id',)
    search_fields = ('pessoa__nome', 'id',)
    raw_id_fields = ('cliente',)

   # class Media:
       # js = (
       #     "//code.jquery.com/jquery-1.11.3.min.js",
       # )



    def valor_br(self, obj):
        return moeda_brasileira(obj.valor)

    def nome(self, obj):
        return obj.pessoa.nome

    def cliente(self, obj):
        return obj.cliente.pessoa.nome


    valor_br.short_description = 'Valor'
    nome.short_description = 'Emissor do Recibo'
    Recibo.file_b.short_description = 'Recibo em Branco'


    def save_model(self, request, obj, form, change):



        #Adicionar Pessoa que está emitindo o Recibo
        obj.pessoa = Pessoa.objects.get(user__id=request.user.id)

        obj.save()

        obj.recibo_branco = "media/Recibos/" + str(obj.id)+'.pdf'

        if obj.recibo_assinado != "":
            obj.recibo_assinado = "media/RecibosAssinados/" + str(obj.id) + "_assinado.pdf"

        obj.save()

        self.emitir_recibo(obj)

    def emitir_recibo(self, recibo):


        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RightAlign', fontName='Helvetica', alignment=TA_RIGHT))
        styles.add(ParagraphStyle(name='LeftAlign', fontName='Helvetica', alignment=TA_LEFT, fontSize=11))
        styles.add(ParagraphStyle(name='CenterAlign', fontName='Helvetica', alignment=TA_CENTER, fontSize=11))
        styles.add(ParagraphStyle(name='CenterAlignH', fontName='Helvetica', alignment=TA_CENTER, leading=16, fontSize=14))

        def cabecalho():
            story = []
            story.append(Paragraph("<b>Alphatux Networking</b>", styles['CenterAlignH']))
            story.append(Paragraph("Ferreira Pontes Comunicações Ltda - ME", styles['CenterAlign']))
            story.append(Paragraph("Rua Inácio Motta, 818 - CEP:. 96130-000 - Colônia Z3 - Pelotas - RS ", styles['CenterAlign']))
            story.append(Paragraph("Contatos:. (53) 3226-0036 / (53) 9114-5689", styles['CenterAlign']))
            return story

        def numero_recibo():
            story = []
            story.append(Paragraph("<b>RECIBO Nº: " + str(recibo.id) + "</b>", styles['LeftAlign']))
            return story

        def valor_recibo():
            story = []
            story.append(Paragraph("<b>" + self.valor_br(recibo) + "</b>", styles['LeftAlign']))
            return story

        def nome_cliente():
            story = []
            story.append(Paragraph("Recebemos do(a) Sr(a): <b>" + recibo.cliente.pessoa.nome + "</b>", styles['LeftAlign']))
            return story

        def valor_descrito():
            story = []
            valor = str(recibo.valor)
            extenso = title_except(dExtenso.dExtenso().to_currency(valor))
            story.append(Paragraph("A Importância de: <b>" + extenso + "</b>", styles['LeftAlign']))
            return story

        def descricao_recibo():
            story = []
            story.append(Paragraph("Referente a: <b>" + recibo.observacoes + "</b>", styles['LeftAlign']))
            #story.append(Paragraph("ID: <b>" + str(self.teste.id) + "</b>", styles['LeftAlign']))
            return story

        def data():
            story = []
            # O Formats deve receber um datetime.datetime, se precisar mostrar hora, usar "DATETIME_FORMATS"
            data_formatada = formats.date_format(recibo.data_emissao, "DATE_FORMAT")
            story.append(Paragraph("<b>Pelotas, " + data_formatada + "</b>", styles['CenterAlign']))
            return story

        def assinatura_emissor():
            story = []
            story.append(Paragraph("<b>" + recibo.pessoa.nome + "</b>", styles['CenterAlign']))
            story.append(Paragraph("<b> Alphatux Networking </b>", styles['CenterAlign']))
            return story

        def assinatura_cliente():
            story = []
            story.append(Paragraph("<b>" + recibo.cliente.pessoa.nome + "</b>", styles['CenterAlign']))
            story.append(Paragraph("<b> Cliente </b>", styles['CenterAlign']))
            return story

        #//TODO: Fazer com que o django crie o diretório, pois o ReportLab não o faz
        c = canvas.Canvas("media/Recibos/" + str(recibo.id)+'.pdf')

        # Frame Corpo de baixo
        f = Frame(1*cm, 0.5*cm, 19*cm, 13.5*cm, showBoundary=1)

        # Frame Corpo de cima
        h = Frame(1*cm, 15.5*cm, 19*cm, 13.5*cm, showBoundary=1)

        # Frame Cabeçalho Cima
        f_cabecalho_cima = Frame(1*cm, 26.5*cm, 19*cm, 2.5*cm, showBoundary=1)

        # Frame Cabeçalho Baixo
        f_cabecalho_baixo = Frame(1*cm, 11.5*cm, 19*cm, 2.5*cm, showBoundary=1)

        # Frame numero recibo baixo
        f_numero_recibo_baixo = Frame(1.3*cm, 10.5*cm, 5*cm, 1*cm, showBoundary=1)

        # Frame numero recibo cima
        f_numero_recibo_cima = Frame(1.3*cm, 25.5*cm, 5*cm, 1*cm, showBoundary=1)

        # Frame valor recibo baixo
        f_valor_recibo_baixo = Frame(15.7*cm, 10.5*cm, 4.3*cm, 1*cm, showBoundary=1)

        # Frame valor recibo cima
        f_valor_recibo_cima = Frame(15.7*cm, 25.5*cm, 4.3*cm, 1*cm, showBoundary=1)

        # Frame nome cliente baixo
        f_nome_cliente_baixo = Frame(1*cm, 9.5*cm, 19*cm, 1*cm, showBoundary=1)

        # Frame nome cliente cima
        f_nome_cliente_cima = Frame(1*cm, 24.5*cm, 19*cm, 1*cm, showBoundary=1)

        # Frame valor descrito baixo
        f_valor_extenso_baixo = Frame(1*cm, 8.5*cm, 19*cm, 1*cm, showBoundary=1)

        # Frame valor descrito cima
        f_valor_extenso_cima = Frame(1*cm, 23.5*cm, 19*cm, 1*cm, showBoundary=1)

        # Frame descrição recibo baixo
        f_descricao_recibo_baixo = Frame(1*cm, 5.5*cm, 19*cm, 3*cm, showBoundary=1)

        # Frame descrição recibo cima
        f_descricao_recibo_cima = Frame(1*cm, 20.5*cm, 19*cm, 3*cm, showBoundary=1)

        # Frame data emissao baixo
        f_data_emissao_baixo = Frame(12*cm, 4.5*cm, 8*cm, 1*cm, showBoundary=1)

        # Frame data emissao cima
        f_data_emissao_cima = Frame(12*cm, 19.5*cm, 8*cm, 1*cm, showBoundary=1)

        # Frame assinatura emissor baixo
        f_assinatura_emissor_baixo = Frame(1*cm, 1.5*cm, 19*cm, 1.5*cm, showBoundary=0)

        # Frame assinatura cliente cima
        f_assinatura_cliente_cima = Frame(1*cm, 16.5*cm, 19*cm, 1.5*cm, showBoundary=0)



        f.addFromList("",c)
        h.addFromList("",c)

        f_cabecalho_baixo.addFromList(cabecalho(),c)
        f_cabecalho_cima.addFromList(cabecalho(),c)

        f_numero_recibo_baixo.addFromList(numero_recibo(), c)
        f_numero_recibo_cima.addFromList(numero_recibo(), c)

        f_valor_recibo_baixo.addFromList(valor_recibo(), c)
        f_valor_recibo_cima.addFromList(valor_recibo(), c)

        f_nome_cliente_baixo.addFromList(nome_cliente(), c)
        f_nome_cliente_cima.addFromList(nome_cliente(), c)

        f_valor_extenso_baixo.addFromList(valor_descrito(), c)
        f_valor_extenso_cima.addFromList(valor_descrito(), c)

        f_descricao_recibo_baixo.addFromList(descricao_recibo(), c)
        f_descricao_recibo_cima.addFromList(descricao_recibo(), c)

        f_data_emissao_baixo.addFromList(data(), c)
        f_data_emissao_cima.addFromList(data(), c)

        f_assinatura_emissor_baixo.addFromList(assinatura_emissor(), c)
        f_assinatura_cliente_cima.addFromList(assinatura_cliente(), c)

        # Linha assinatura emissor
        c.line(5*cm, 3*cm, 16*cm, 3*cm)
        # Linha assinatura cliente
        c.line(5*cm, 18*cm, 16*cm, 18*cm)

        c.setDash(2,2)
        c.line(1*mm, 14.7*cm, 21*cm, 14.7*cm)

        c.save()

###################################################################################################

