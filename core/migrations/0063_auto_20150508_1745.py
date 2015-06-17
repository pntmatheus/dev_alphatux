# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20150508_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recibo',
            options={'ordering': ['id'], 'verbose_name_plural': 'Recibos', 'verbose_name': 'Recibo'},
        ),
    ]
