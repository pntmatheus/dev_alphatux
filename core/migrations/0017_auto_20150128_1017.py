# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='abreviacao',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
