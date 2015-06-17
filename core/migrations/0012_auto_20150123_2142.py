# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150123_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ap',
            name='mac_lan',
        ),
        migrations.AddField(
            model_name='ap',
            name='arquivo_conf',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ap',
            name='mac_ethernet',
            field=models.CharField(blank=True, max_length=17),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ap',
            name='senha_wpa',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ap',
            name='firmware',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
