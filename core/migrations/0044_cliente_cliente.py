# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20150430_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cliente',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
    ]
