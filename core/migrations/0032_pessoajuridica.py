# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_pessoafisica'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100, blank=True)),
                ('cnpj', models.CharField(max_length=18)),
                ('inscricao_estadual', models.CharField(max_length=15, blank=True)),
                ('inscricao_municipal', models.CharField(max_length=15, blank=True)),
                ('abertura_empresa', models.DateField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Pessoas Juridica',
                'verbose_name': 'Pessoa Juridica',
            },
            bases=(models.Model,),
        ),
    ]
