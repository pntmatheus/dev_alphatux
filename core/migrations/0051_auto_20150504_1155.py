# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20150430_1942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['pessoa__nome'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]
