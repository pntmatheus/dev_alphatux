# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_auto_20150508_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='data_emissao',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
