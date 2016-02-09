# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160131_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco2',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='endereco2',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='endereco2',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='endereco2',
            name='rua',
        ),
        migrations.AddField(
            model_name='cep',
            name='bairro',
            field=smart_selects.db_fields.ChainedForeignKey(default='', to='core.Bairro', chained_field='cidade', auto_choose=True, chained_model_field='cidade'),
        ),
        migrations.AddField(
            model_name='cep',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(default='', to='core.Cidade', chained_field='estado', auto_choose=True, chained_model_field='estado'),
        ),
        migrations.AddField(
            model_name='cep',
            name='estado',
            field=models.ForeignKey(to='core.Estado', default=''),
        ),
        migrations.AlterField(
            model_name='cep',
            name='codigo',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterField(
            model_name='cep',
            name='rua',
            field=smart_selects.db_fields.ChainedForeignKey(default='', to='core.Rua', chained_field='bairro', auto_choose=True, chained_model_field='bairro'),
        ),
        migrations.DeleteModel(
            name='Endereco2',
        ),
    ]
