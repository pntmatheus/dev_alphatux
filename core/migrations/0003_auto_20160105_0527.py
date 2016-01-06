# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160105_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nome_fantasia',
            field=models.CharField(max_length=100, verbose_name='Apelido/Nome Fantasia', blank=True),
        ),
    ]
