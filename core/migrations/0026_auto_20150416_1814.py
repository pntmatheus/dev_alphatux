# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20150412_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distribuidorinterno',
            old_name='ip_lan',
            new_name='senha_wpa',
        ),
        migrations.RemoveField(
            model_name='distribuidorinterno',
            name='foto_distribuidor_interno',
        ),
        migrations.RemoveField(
            model_name='distribuidorinterno',
            name='password',
        ),
        migrations.RemoveField(
            model_name='distribuidorinterno',
            name='user',
        ),
        migrations.RemoveField(
            model_name='distribuidorinterno',
            name='wpa',
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='firmware',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='senha',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='usuario',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
    ]
