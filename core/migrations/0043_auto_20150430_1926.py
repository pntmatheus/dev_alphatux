# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20150430_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cliente_desde',
            field=models.DateField(default='1989-02-27'),
            preserve_default=True,
        ),
    ]
