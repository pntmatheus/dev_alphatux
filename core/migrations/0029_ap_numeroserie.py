# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20150416_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='ap',
            name='numeroSerie',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
    ]
