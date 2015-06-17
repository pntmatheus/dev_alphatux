# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20150425_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=15, blank=True)),
                ('apelido', models.CharField(max_length=100, blank=True)),
                ('data_nascimento', models.DateField(blank=True)),
            ],
            options={
                'verbose_name': 'Pessoa Fisica',
                'verbose_name_plural': 'Pessoas Fisica',
            },
            bases=(models.Model,),
        ),
    ]
