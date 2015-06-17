# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20150430_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apelido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='logradouro',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nome_dump',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='observacoes',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='rg',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone1',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone2',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cliente_desde',
            field=models.DateField(default='1989-02-27'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='pessoa',
            field=models.OneToOneField(to='core.Pessoa', default=''),
            preserve_default=True,
        ),
    ]
