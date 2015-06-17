# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20150427_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='pessoa_fisica',
        ),
        migrations.DeleteModel(
            name='PessoaFisica',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='pessoa_juridica',
        ),
        migrations.DeleteModel(
            name='PessoaJuridica',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='inscricao_estadual',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='inscricao_municipal',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='rg',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
