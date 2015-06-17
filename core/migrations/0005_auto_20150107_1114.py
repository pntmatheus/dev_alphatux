# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150106_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pop',
            field=models.ForeignKey(to='core.Pop'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='foto_dispositivo_cliente',
            field=models.ImageField(upload_to='uploads'),
            preserve_default=True,
        ),
    ]
