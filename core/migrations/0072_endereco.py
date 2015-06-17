# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_auto_20150607_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('cidade', smart_selects.db_fields.ChainedForeignKey(to='core.Estado', chained_field=models.ForeignKey(to='core.Estado', related_name='+'))),
                ('estado', models.ForeignKey(to='core.Estado', related_name='+')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
            bases=(models.Model,),
        ),
    ]
