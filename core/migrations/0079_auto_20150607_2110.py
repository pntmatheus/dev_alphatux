# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_auto_20150607_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field=models.ForeignKey(to='core.Estado'), to='core.Cidade', chained_model_field='estado'),
            preserve_default=True,
        ),
    ]
