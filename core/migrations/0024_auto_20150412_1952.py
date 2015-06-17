# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20150412_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='ap',
            name='senha',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ap',
            name='usuario',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ap',
            name='ip_acesso',
            field=models.GenericIPAddressField(),
            preserve_default=True,
        ),
    ]
