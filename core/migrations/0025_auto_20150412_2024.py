# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20150412_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nota_fiscal',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='numero_residencial',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='pop',
        ),
        migrations.AddField(
            model_name='cliente',
            name='foto_cliente',
            field=models.ImageField(blank=True, upload_to='Clientes/fotos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='logradouro',
            field=models.OneToOneField(to='core.Logradouro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apelido',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome_dump',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observacoes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone2',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
    ]
