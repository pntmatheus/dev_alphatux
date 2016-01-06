# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='codigo',
            field=models.CharField(max_length=18, default='', verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
