# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import os
import datetime
from smart_selects.db_fields import ChainedForeignKey

class Fabricante(models.Model):
    class Meta():
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    class Meta():
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
    modelo = models.CharField(max_length=100)
    fabricante = models.ForeignKey(Fabricante)

    def __str__(self):
        return self.modelo

class TipoPessoa(models.Model):
    class Meta():
        verbose_name = 'TipoPessoa'
        verbose_name_plural = 'TipoPessoas'

    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class TipoPolaridade(models.Model):
    class Meta():
        verbose_name = 'TipoPolaridade'
        verbose_name_plural = 'TipoPolaridades'

    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Estado(models.Model):
    class Meta():
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    nome = models.CharField(max_length=50)
    abreviacao = models.CharField(max_length=2)

    def __str__(self):
        return self.abreviacao


class Cidade(models.Model):
    class Meta():
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado)

    def __str__(self):
        return self.nome


class Bairro(models.Model):
    class Meta():
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade)

    def __str__(self):
        return self.nome


class TipoEndereco(models.Model):
    class Meta():
        verbose_name = 'TipoEndereco'
        verbose_name_plural = 'TipoEnderecos'

    nome = models.CharField(max_length=50)
    abreviacao = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Rua(models.Model):
    class Meta():
        verbose_name = 'Rua'
        verbose_name_plural = 'Ruas'

    nome = models.CharField(max_length=50)
    bairro = models.ForeignKey(Bairro)
    tipo_endereco = models.ForeignKey(TipoEndereco)

    def __str__(self):
        return self.tipo_endereco.abreviacao + " " + self.nome


class Cep(models.Model):
    class Meta():
        verbose_name = 'Cep'
        verbose_name_plural = 'Ceps'

    codigo = models.CharField(max_length=9)
    rua = models.ForeignKey(Rua, null=True)

    def __str__(self):
        return self.codigo

class Endereco(models.Model):
    class Meta():
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


    estado = models.ForeignKey(Estado)
    cidade = ChainedForeignKey(Cidade, chained_field="estado", chained_model_field="estado", auto_choose=True)
    bairro = ChainedForeignKey(Bairro, chained_field="cidade", chained_model_field="cidade", auto_choose=True)
    rua = ChainedForeignKey(Rua, chained_field="bairro", chained_model_field="bairro", auto_choose=True)
    cep = ChainedForeignKey(Cep, chained_field="rua", chained_model_field="rua", auto_choose=True)
    numero = models.CharField(max_length=10, default='')
    complemento = models.CharField(max_length=20, blank=True)

    def get_nome(self):
        return str(self.estado) + ' - ' + str(self.cidade) + ' - ' + str(self.bairro) + ' - ' + str(self.rua) + ' - Nº' + str(self.numero) +  '- CEP:' + ' ' + str(self.cep)

    def __str__(self):
        return str(self.estado) + ' - ' + str(self.cidade) + ' - ' + str(self.bairro) + ' - ' + str(self.rua) + ' - Nº' + str(self.numero) +  '- CEP:' + ' ' + str(self.cep)

class Pessoa(models.Model):
    class Meta():
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    nome = models.CharField(max_length=100, default='')
    ### CPF/CPNJ ###
    codigo = models.CharField(max_length=18, default='')
    ### APELIDO/NOME FANTASIA ###
    nome_fantasia = models.CharField(max_length=100, blank=True)
    telefone1 = models.CharField(max_length=20)
    telefone2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    observacoes = models.TextField(blank=True)
    tipo_pessoa = models.ForeignKey(TipoPessoa)
    rg = models.CharField(max_length=15, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=15, blank=True)
    inscricao_municipal = models.CharField(max_length=15, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True)
    #### Coluna para utilizar no search_field sem acentuacao
    search_dump = models.CharField(max_length=255, default='', blank=True, editable=False)

    def __str__(self):
        return self.nome

    def get_nome(self):
        return self.nome


class Pop(models.Model):
    class Meta():
        verbose_name = 'Pop'

    nome = models.CharField(max_length=100)
    foto_pop = models.ImageField(upload_to='POPs/fotos', blank=True)
    endereco = models.ForeignKey(Endereco, null=True)

    def image_(self):
        return '<a href="/media/{0}"><img src="/media/{0}" width="100" height="100"></a>'.format(self.foto_pop)

    image_.allow_tags = True

    def __str__(self):
        return self.nome


class AP(models.Model):
    class Meta():
        verbose_name = 'AP'
        verbose_name_plural = 'Aps'

    fabricante = models.ForeignKey(Fabricante, null=True)
    equipamento = ChainedForeignKey(Equipamento, chained_field="fabricante", chained_model_field="fabricante", auto_choose=True, null=True)
    firmware = models.CharField(max_length=50, blank=True)
    ip_acesso = models.GenericIPAddressField(protocol='both')
    mac_ethernet = models.CharField(max_length=17, blank=True)
    mac_wireless = models.CharField(max_length=17)
    ssid = models.CharField(max_length=50)
    senha_wpa = models.CharField(max_length=50, blank=True)
    foto_ap = models.ImageField(upload_to='APs/fotos', blank=True)
    arquivo_conf = models.FileField(upload_to='APs/arquivos', blank=True)
    usuario = models.CharField(max_length=50, default='')
    senha = models.CharField(max_length=50, default='')
    numero_serie = models.CharField(max_length=50, blank=True, default='')
    pop = models.ForeignKey(Pop)
    tipo_polaridade = models.ForeignKey(TipoPolaridade)

    def image_(self):
        return '<a href="/media/{0}"><img src="/media/{0}" width="100" height="100"></a>'.format(self.foto_ap)

    image_.allow_tags = True

    def file_(self):
        return '<a href="/media/{0}"><img src="/media/{0}" width="100" height="100"></a>'.format(self.arquivo_conf)

    file_.allow_tags = True

    def __str__(self):
        return self.ssid


class Cliente(models.Model):
    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['pessoa__nome']

    cliente_desde = models.DateField()
    foto_cliente = models.ImageField(upload_to='Clientes/fotos', blank=True)
    pessoa = models.OneToOneField(Pessoa)

    def nome_cliente(self):
        return self.pessoa.nome

    def apelido_cliente(self):
        return self.pessoa.nome_fantasia

    def image_(self):
        return '<a href="/media/{0}"><img src="/media/{0}" width="100" height="100"></a>'.format(self.foto_cliente)

    image_.allow_tags = True

    def __str__(self):
        return self.pessoa.nome


class DistribuidorInterno(models.Model):
    class Meta():
        verbose_name = 'Distribuidor interno'
        verbose_name_plural = 'Distribuidores internos'

    fabricante = models.ForeignKey(Fabricante, null=True)
    equipamento = ChainedForeignKey(Equipamento, chained_field="fabricante", chained_model_field="fabricante", auto_choose=True, null=True)
    firmware = models.CharField(max_length=50, blank=True)
    ssid = models.CharField(max_length=50)
    senha_wpa = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50, blank=True)
    senha = models.CharField(max_length=50, blank=True)
    numero_serie = models.CharField(max_length=50, blank=True, default='')
    endereco = models.ForeignKey(Endereco, null=True)
    pessoa = models.ForeignKey(Pessoa, verbose_name="dono")
    cliente = models.ForeignKey(Cliente, null=True,blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.equipamento.modelo


class Plano(models.Model):
    class Meta():
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    nome = models.CharField(max_length=50)
    upload = models.CharField(max_length=10)
    download = models.CharField(max_length=10)
    valor = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class DispositivoCliente(models.Model):
    class Meta():
        verbose_name = 'Dispositivo do cliente'
        verbose_name_plural = 'Dispositivos do cliente'

    # Vencimento de 1 a 28( por causa do Fevereiro )
    CHOICES = [(i,i) for i in range(29)]


    fabricante = models.ForeignKey(Fabricante, null=True)
    equipamento = ChainedForeignKey(Equipamento, chained_field="fabricante", chained_model_field="fabricante", auto_choose=True, null=True)
    firmware = models.CharField(max_length=50, blank=True)
    mac_wan = models.CharField(max_length=17)
    foto_instalacao = models.ImageField(upload_to='DispositivoCliente/fotos', blank=True)
    usuario = models.CharField(max_length=50, blank=True)
    senha = models.CharField(max_length=50, blank=True)
    vencimento = models.IntegerField(null=True, choices=CHOICES)
    arquivo_conf = models.FileField(upload_to='APs/arquivos', blank=True)
    numero_serie = models.CharField(max_length=50, blank=True, default='')
    ativo = models.BooleanField(default=False)
    endereco = models.ForeignKey(Endereco, null=True)
    ap = models.ForeignKey(AP)
    plano = models.ForeignKey(Plano, default='')
    pessoa = models.ForeignKey(Pessoa, verbose_name="dono")
    cliente = models.ForeignKey(Cliente, null=True,blank=True, on_delete=models.SET_NULL)
    tipo_polaridade = models.ForeignKey(TipoPolaridade)

    def file_(self):
        return '<a href="/media/{0}"><img src="/media/{0}" width="100" height="100"></a>'.format(self.arquivo_conf)

    file_.allow_tags = True

    def foto_dispositivo(self):
        return '<a href="/media/{0}"><img src="/media/{0}" width="100" height="100"></a>'.format(self.foto_instalacao)

    foto_dispositivo.allow_tags = True

    def __str__(self):
        return self.equipamento.modelo



def content_file_name(instance, filename):
        ext = filename.split('.')[-1]
        name = str(instance.id) + "_assinado"
        filename = "%s.%s" % (name, ext)
        path = "media/RecibosAssinados/" + str(filename)
        tempo = datetime.datetime.now()
        hora_formatada = "{0}_{1}_{2}_{3}_{4}_{5}".format(tempo.hour, tempo.minute, tempo.second, tempo.day, tempo.month, tempo.year)
        if os.path.exists(path):
            os.renames(path, "media/RecibosAssinados/" + str(name) + "_" + str(hora_formatada) + "." + str(ext))

        return os.path.join('RecibosAssinados', filename)

class Recibo(models.Model):
    class Meta():
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'
        ordering = ['id',]

    competencia = models.DateField(default=datetime.datetime.now)
    observacoes = models.TextField(blank=True, default="Serviços de Internet")
    data_emissao = models.DateTimeField(auto_now=True, editable=False)
    valor = models.DecimalField(decimal_places=2, max_digits=6)
    recibo_assinado = models.FileField(upload_to=content_file_name, blank=True)
    recibo_branco = models.FileField(upload_to='Recibos/', blank=True, editable=False)
    cliente = models.ForeignKey(Cliente)
    pessoa = models.ForeignKey(Pessoa, editable=False)


    def file_(self):
        if self.recibo_assinado == "":
            return "Nenhum"
        else:
            return '<a href="/{0}" target="_blank">{1}_assinado.pdf</a>'.format(self.recibo_assinado, self.id)

    def file_b(self):
        return '<a href="/{0}" target="_blank">{1}.pdf</a>'.format(self.recibo_branco, self.id)

    file_.allow_tags = True

    file_b.allow_tags = True


    def __str__(self):
        return str(self.id)

