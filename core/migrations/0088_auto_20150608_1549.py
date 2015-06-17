# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0087_remove_pessoa_logradouro'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='search_field_nome_nome_fantasia',
            field=models.CharField(blank=True, max_length=255, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_desde',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
