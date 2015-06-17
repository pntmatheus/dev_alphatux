# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_ap_firmware'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='firmware',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
