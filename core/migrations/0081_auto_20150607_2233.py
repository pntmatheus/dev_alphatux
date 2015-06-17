# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_auto_20150607_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='bairro',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='cidade', null=True, chained_field='cidade', to='core.Bairro', auto_choose=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='rua',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='bairro', null=True, chained_field='bairro', to='core.Rua', auto_choose=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='estado', chained_model_field='estado', to='core.Cidade', auto_choose=True),
            preserve_default=True,
        ),
    ]
