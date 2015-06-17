# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_auto_20150607_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cep',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='cep', to='core.Cep', null=True, chained_field='cep', auto_choose=True),
            preserve_default=True,
        ),
    ]
