# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_endereco_cep'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='numero',
            field=models.CharField(max_length=10, default=''),
            preserve_default=True,
        ),
    ]
