# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160131_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cep',
            name='bairro',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='cidade', chained_model_field='cidade', to='core.Bairro', auto_choose=True),
        ),
        migrations.AlterField(
            model_name='cep',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='estado', chained_model_field='estado', to='core.Cidade', auto_choose=True),
        ),
        migrations.AlterField(
            model_name='cep',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cep',
            name='estado',
            field=models.ForeignKey(to='core.Estado'),
        ),
        migrations.AlterField(
            model_name='cep',
            name='rua',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='bairro', chained_model_field='bairro', to='core.Rua', auto_choose=True),
        ),
    ]
