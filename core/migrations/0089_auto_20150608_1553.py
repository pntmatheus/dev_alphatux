# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0088_auto_20150608_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='search_field_nome_nome_fantasia',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='search_dump',
            field=models.CharField(max_length=255, default='', blank=True, editable=False),
            preserve_default=True,
        ),
    ]
