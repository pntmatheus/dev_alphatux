# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150107_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuidorinterno',
            name='foto_distribuidor_interno',
            field=models.ImageField(upload_to=''),
            preserve_default=True,
        ),
    ]
