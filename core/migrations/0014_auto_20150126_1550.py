# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_ap_foto_ap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='foto_ap',
            field=models.ImageField(upload_to='teste'),
            preserve_default=True,
        ),
    ]
