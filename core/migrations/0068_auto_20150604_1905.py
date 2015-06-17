# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20150604_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(to='core.Estado'),
            preserve_default=True,
        ),
    ]
