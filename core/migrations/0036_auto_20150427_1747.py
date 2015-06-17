# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20150426_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='codigo',
            field=models.CharField(max_length=18, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nome_fantasia',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
