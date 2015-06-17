# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_auto_20150607_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(to='core.Estado', chained_model_field='estado', chained_field=models.ForeignKey(to='core.Estado', related_name='+'), auto_choose=True),
            preserve_default=True,
        ),
    ]
