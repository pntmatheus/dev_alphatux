# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_pessoajuridica'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'TipoPessoa',
                'verbose_name_plural': 'TipoPessoas',
            },
            bases=(models.Model,),
        ),
    ]
