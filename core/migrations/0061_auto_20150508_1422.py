# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_recibo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='data_emissao',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
    ]
