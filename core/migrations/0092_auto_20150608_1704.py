# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_auto_20150608_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Equipamentos',
                'verbose_name': 'Equipamento',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Fabricantes',
                'verbose_name': 'Fabricante',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='fabricante',
            field=models.ForeignKey(to='core.Fabricante'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='ap',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='dispositivocliente',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='distribuidorinterno',
            name='modelo',
        ),
        migrations.AddField(
            model_name='ap',
            name='equipamento',
            field=smart_selects.db_fields.ChainedForeignKey(null=True, to='core.Equipamento', chained_field='fabricante', auto_choose=True, chained_model_field='fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='equipamento',
            field=smart_selects.db_fields.ChainedForeignKey(null=True, to='core.Equipamento', chained_field='fabricante', auto_choose=True, chained_model_field='fabricante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='equipamento',
            field=smart_selects.db_fields.ChainedForeignKey(null=True, to='core.Equipamento', chained_field='fabricante', auto_choose=True, chained_model_field='fabricante'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ap',
            name='fabricante',
            field=models.ForeignKey(to='core.Fabricante', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='fabricante',
            field=models.ForeignKey(to='core.Fabricante', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='distribuidorinterno',
            name='fabricante',
            field=models.ForeignKey(to='core.Fabricante', null=True),
            preserve_default=True,
        ),
    ]
