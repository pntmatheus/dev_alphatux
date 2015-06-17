# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20150604_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logradouro',
            name='rua',
            field=models.ForeignKey(to='core.Rua'),
            preserve_default=True,
        ),
    ]
