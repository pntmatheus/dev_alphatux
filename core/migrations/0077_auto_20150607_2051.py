# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_auto_20150607_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='core.Cidade', chained_model_field='Estado', chained_field=models.ForeignKey(to='core.Estado')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.ForeignKey(to='core.Estado'),
            preserve_default=True,
        ),
    ]
