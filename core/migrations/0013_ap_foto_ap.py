# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150123_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='ap',
            name='foto_ap',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
