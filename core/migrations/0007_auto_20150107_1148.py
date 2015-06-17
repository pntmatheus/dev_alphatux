# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150107_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivocliente',
            name='foto_dispositivo_cliente',
            field=models.ImageField(upload_to=''),
            preserve_default=True,
        ),
    ]
