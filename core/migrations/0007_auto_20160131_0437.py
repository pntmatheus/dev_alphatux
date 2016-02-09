# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160131_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='rua',
        ),
        migrations.AddField(
            model_name='endereco',
            name='latitude',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='longitude',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
