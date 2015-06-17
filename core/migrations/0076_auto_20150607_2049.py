# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_auto_20150607_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='Estado', auto_choose=True, chained_field=models.ForeignKey(related_name='estado', to='core.Estado'), to='core.Estado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.ForeignKey(related_name='estado', to='core.Estado'),
            preserve_default=True,
        ),
    ]
