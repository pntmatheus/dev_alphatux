# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_endereco_search_dump'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='search_dump',
        ),
        migrations.AddField(
            model_name='rua',
            name='search_dump',
            field=models.CharField(max_length=255, default='', blank=True, editable=False),
        ),
    ]
