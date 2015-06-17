# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ip_acesso', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=50)),
                ('mac_lan', models.CharField(max_length=17)),
                ('ssid', models.CharField(max_length=50)),
                ('fabricante', models.CharField(max_length=50)),
                ('mac_wireless', models.CharField(max_length=17)),
            ],
            options={
                'verbose_name_plural': 'Aps',
                'verbose_name': 'AP',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=100)),
                ('nome_dump', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('telefone1', models.CharField(max_length=20)),
                ('telefone2', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
                ('numero_residencial', models.IntegerField(null=True)),
                ('cep', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=15)),
                ('nota_fiscal', models.CharField(max_length=50)),
                ('observacoes', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DispositivoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fabricante', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('endereco_mac', models.CharField(max_length=17)),
                ('foto_dispositivo_cliente', models.FileField(upload_to='')),
                ('situacao', models.CharField(max_length=50)),
                ('vencimento', models.CharField(max_length=50)),
                ('ap', models.ForeignKey(to='core.AP')),
                ('cliente', models.ForeignKey(to='core.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Dispositivos do cliente',
                'verbose_name': 'Dispositivo do cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DistribuidorInterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fabricante', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ssid', models.CharField(max_length=50)),
                ('wpa', models.CharField(max_length=50)),
                ('foto_distribuidor_interno', models.FileField(upload_to='')),
                ('ip_lan', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(to='core.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Distribuidores Internos',
                'verbose_name': 'Distribuidor Interno',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('upload', models.CharField(max_length=10)),
                ('valor', models.CharField(max_length=10)),
                ('download', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=50)),
                ('disposito_cliente', models.OneToOneField(to='core.DispositivoCliente')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Pop',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsuarioSistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('perfil', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Usuários do Sistema',
                'verbose_name': 'Usuário do Sistema',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='pop',
            field=models.ForeignKey(to='core.Pop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ap',
            name='pop',
            field=models.ForeignKey(to='core.Pop'),
            preserve_default=True,
        ),
    ]
