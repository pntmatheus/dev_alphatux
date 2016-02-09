# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160105_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('cep', models.CharField(max_length=10, default='')),
                ('bairro', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cidade', to='core.Bairro', chained_model_field='cidade')),
                ('cidade', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='estado', to='core.Cidade', chained_model_field='estado')),
                ('estado', models.ForeignKey(to='core.Estado')),
                ('rua', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='bairro', to='core.Rua', chained_model_field='bairro')),
            ],
            options={
                'verbose_name_plural': 'Endereços2',
                'verbose_name': 'Endereço2',
            },
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='inscricao_estadual',
            field=models.CharField(max_length=15, verbose_name='Inscrição Estadual', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='inscricao_municipal',
            field=models.CharField(max_length=15, verbose_name='Inscrição Municipal', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='observacoes',
            field=models.TextField(verbose_name='Observações', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='rg',
            field=models.CharField(max_length=15, verbose_name='RG', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone1',
            field=models.CharField(max_length=20, verbose_name='Telefone Principal'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone2',
            field=models.CharField(max_length=20, verbose_name='Outro Telefone', blank=True),
        ),
    ]
