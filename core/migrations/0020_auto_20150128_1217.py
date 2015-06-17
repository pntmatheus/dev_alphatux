# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_bairro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=20, blank=True)),
                ('bairro', models.ForeignKey(to='core.Bairro')),
            ],
            options={
                'verbose_name': 'Logradouro',
                'verbose_name_plural': 'Logradouros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEndereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('abreviacao', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'TipoEndereco',
                'verbose_name_plural': 'TipoEnderecos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='logradouro',
            name='tipo_endereco',
            field=models.ForeignKey(to='core.TipoEndereco'),
            preserve_default=True,
        ),
    ]
