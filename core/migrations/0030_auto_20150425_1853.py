# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_ap_numeroserie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='numeroSerie',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=True,
        ),
    ]
