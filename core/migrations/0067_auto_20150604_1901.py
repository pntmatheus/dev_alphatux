# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20150601_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='estado',
            field=smart_selects.db_fields.ChainedForeignKey(to='core.Estado'),
            preserve_default=True,
        ),
    ]
