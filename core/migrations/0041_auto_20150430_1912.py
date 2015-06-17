# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20150430_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pop',
            name='logradouro',
            field=models.ForeignKey(to='core.Logradouro'),
            preserve_default=True,
        ),
    ]
