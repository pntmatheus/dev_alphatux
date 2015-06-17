# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150123_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='firmware',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
