# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_auto_20150604_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('bairro', models.ForeignKey(to='core.Bairro')),
                ('tipo_endereco', models.ForeignKey(to='core.TipoEndereco')),
            ],
            options={
                'verbose_name_plural': 'Ruas',
                'verbose_name': 'Rua',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='logradouro',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='logradouro',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='logradouro',
            name='tipo_endereco',
        ),
        migrations.AddField(
            model_name='logradouro',
            name='rua',
            field=models.ForeignKey(null=True, to='core.Rua', blank=True),
            preserve_default=True,
        ),
    ]
