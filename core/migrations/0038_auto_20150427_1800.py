# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20150427_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoafisica',
            options={},
        ),
        migrations.AlterModelOptions(
            name='pessoajuridica',
            options={},
        ),
        migrations.RemoveField(
            model_name='pessoajuridica',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='pessoajuridica',
            name='nome_fantasia',
        ),
        migrations.RemoveField(
            model_name='pessoajuridica',
            name='razao_social',
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='pessoa_fisica',
            field=models.OneToOneField(to='core.PessoaFisica', blank=True, on_delete='CASCADE', null=True),
            preserve_default=True,
        ),
    ]
