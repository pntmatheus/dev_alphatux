# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0094_auto_20150630_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='ip_acesso',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
