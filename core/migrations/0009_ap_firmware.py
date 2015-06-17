# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150107_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='ap',
            name='firmware',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
