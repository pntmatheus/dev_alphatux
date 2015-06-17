# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_auto_20150604_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cep',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('codigo', models.CharField(max_length=9)),
                ('ruas', models.ManyToManyField(to='core.Rua')),
            ],
            options={
                'verbose_name': 'Cep',
                'verbose_name_plural': 'Ceps',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='logradouro',
            name='cep',
            field=models.ForeignKey(to='core.Cep'),
            preserve_default=True,
        ),
    ]
