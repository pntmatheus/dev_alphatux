# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(to='core.Estado', auto_choose=True, chained_field=models.ForeignKey(to='core.Estado', related_name='+')),
            preserve_default=True,
        ),
    ]
