# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime
import smart_selects.db_fields
import core.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AP',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('firmware', models.CharField(blank=True, max_length=50)),
                ('ip_acesso', models.CharField(max_length=50)),
                ('mac_ethernet', models.CharField(blank=True, max_length=17)),
                ('mac_wireless', models.CharField(max_length=17)),
                ('ssid', models.CharField(max_length=50)),
                ('senha_wpa', models.CharField(blank=True, max_length=50)),
                ('foto_ap', models.ImageField(blank=True, upload_to='APs/fotos')),
                ('arquivo_conf', models.FileField(blank=True, upload_to='APs/arquivos')),
                ('usuario', models.CharField(default='', max_length=50)),
                ('senha', models.CharField(default='', max_length=50)),
                ('numero_serie', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Aps',
                'verbose_name': 'AP',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Bairros',
                'verbose_name': 'Bairro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cep',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(max_length=9)),
            ],
            options={
                'verbose_name_plural': 'Ceps',
                'verbose_name': 'Cep',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cidades',
                'verbose_name': 'Cidade',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cliente_desde', models.DateField()),
                ('foto_cliente', models.ImageField(blank=True, upload_to='Clientes/fotos')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
                'ordering': ['pessoa__nome'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DispositivoCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('firmware', models.CharField(blank=True, max_length=50)),
                ('mac_wan', models.CharField(max_length=17)),
                ('foto_instalacao', models.ImageField(blank=True, upload_to='DispositivoCliente/fotos')),
                ('usuario', models.CharField(blank=True, max_length=50)),
                ('senha', models.CharField(blank=True, max_length=50)),
                ('vencimento', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28)], null=True)),
                ('arquivo_conf', models.FileField(blank=True, upload_to='APs/arquivos')),
                ('numero_serie', models.CharField(blank=True, default='', max_length=50)),
                ('ativo', models.BooleanField(default=False)),
                ('ap', models.ForeignKey(to='core.AP')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Dispositivos do cliente',
                'verbose_name': 'Dispositivo do cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DistribuidorInternooo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('firmware', models.CharField(blank=True, max_length=50)),
                ('ssid', models.CharField(max_length=50)),
                ('senha_wpa', models.CharField(max_length=50)),
                ('usuario', models.CharField(blank=True, max_length=50)),
                ('senha', models.CharField(blank=True, max_length=50)),
                ('numero_serie', models.CharField(blank=True, default='', max_length=50)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Distribuidores internos',
                'verbose_name': 'Distribuidor interno',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('numero', models.CharField(default='', max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=20)),
                ('bairro', smart_selects.db_fields.ChainedForeignKey(chained_model_field='cidade', auto_choose=True, to='core.Bairro', chained_field='cidade')),
                ('cep', smart_selects.db_fields.ChainedForeignKey(chained_model_field='rua', auto_choose=True, to='core.Cep', chained_field='rua')),
                ('cidade', smart_selects.db_fields.ChainedForeignKey(chained_model_field='estado', auto_choose=True, to='core.Cidade', chained_field='estado')),
            ],
            options={
                'verbose_name_plural': 'Endereços',
                'verbose_name': 'Endereço',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('modelo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Equipamentos',
                'verbose_name': 'Equipamento',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('abreviacao', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'verbose_name': 'Estado',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Fabricantes',
                'verbose_name': 'Fabricante',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(default='', max_length=100)),
                ('codigo', models.CharField(default='', max_length=18)),
                ('nome_fantasia', models.CharField(blank=True, max_length=100)),
                ('telefone1', models.CharField(max_length=20)),
                ('telefone2', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('observacoes', models.TextField(blank=True)),
                ('rg', models.CharField(blank=True, max_length=15)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=15)),
                ('inscricao_municipal', models.CharField(blank=True, max_length=15)),
                ('search_dump', models.CharField(blank=True, editable=False, default='', max_length=255)),
                ('endereco', models.ForeignKey(null=True, to='core.Endereco')),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'verbose_name': 'Pessoa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('upload', models.CharField(max_length=10)),
                ('download', models.CharField(max_length=10)),
                ('valor', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Planos',
                'verbose_name': 'Plano',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pop',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('foto_pop', models.ImageField(blank=True, upload_to='POPs/fotos')),
                ('endereco', models.ForeignKey(null=True, to='core.Endereco')),
            ],
            options={
                'verbose_name': 'Pop',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('competencia', models.DateField(default=datetime.datetime.now)),
                ('observacoes', models.TextField(blank=True, default='Serviços de Internet')),
                ('data_emissao', models.DateTimeField(auto_now=True)),
                ('valor', models.DecimalField(max_digits=6, decimal_places=2)),
                ('recibo_assinado', models.FileField(blank=True, upload_to=core.models.content_file_name)),
                ('recibo_branco', models.FileField(blank=True, editable=False, upload_to='Recibos/')),
                ('cliente', models.ForeignKey(to='core.Cliente')),
                ('pessoa', models.ForeignKey(editable=False, to='core.Pessoa')),
            ],
            options={
                'verbose_name_plural': 'Recibos',
                'verbose_name': 'Recibo',
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('bairro', models.ForeignKey(to='core.Bairro')),
            ],
            options={
                'verbose_name_plural': 'Ruas',
                'verbose_name': 'Rua',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEndereco',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('abreviacao', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'TipoEnderecos',
                'verbose_name': 'TipoEndereco',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoPessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'TipoPessoas',
                'verbose_name': 'TipoPessoa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoPolaridade',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'TipoPolaridades',
                'verbose_name': 'TipoPolaridade',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rua',
            name='tipo_endereco',
            field=models.ForeignKey(to='core.TipoEndereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tipo_pessoa',
            field=models.ForeignKey(to='core.TipoPessoa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipamento',
            name='fabricante',
            field=models.ForeignKey(to='core.Fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.ForeignKey(to='core.Estado'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='rua',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='bairro', auto_choose=True, to='core.Rua', chained_field='bairro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='endereco',
            field=models.ForeignKey(null=True, to='core.Endereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='equipamento',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='fabricante', null=True, auto_choose=True, to='core.Equipamento', chained_field='fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='fabricante',
            field=models.ForeignKey(null=True, to='core.Fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='pessoa',
            field=models.ForeignKey(to='core.Pessoa', verbose_name='dono'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='endereco',
            field=models.ForeignKey(null=True, to='core.Endereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='equipamento',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='fabricante', null=True, auto_choose=True, to='core.Equipamento', chained_field='fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='fabricante',
            field=models.ForeignKey(null=True, to='core.Fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='pessoa',
            field=models.ForeignKey(to='core.Pessoa', verbose_name='dono'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='plano',
            field=models.ForeignKey(default='', to='core.Plano'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='tipo_polaridade',
            field=models.ForeignKey(to='core.TipoPolaridade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='pessoa',
            field=models.OneToOneField(to='core.Pessoa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(to='core.Estado'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cep',
            name='rua',
            field=models.ForeignKey(null=True, to='core.Rua'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(to='core.Cidade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ap',
            name='equipamento',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='fabricante', null=True, auto_choose=True, to='core.Equipamento', chained_field='fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ap',
            name='fabricante',
            field=models.ForeignKey(null=True, to='core.Fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ap',
            name='pop',
            field=models.ForeignKey(to='core.Pop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ap',
            name='tipo_polaridade',
            field=models.ForeignKey(to='core.TipoPolaridade'),
            preserve_default=True,
        ),
    ]
