# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_auto_20150607_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='cidade', chained_field='cidade', to='core.Bairro', auto_choose=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='rua', chained_field='rua', to='core.Cep', auto_choose=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='rua',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='bairro', chained_field='bairro', to='core.Rua', auto_choose=True),
            preserve_default=True,
        ),
    ]
