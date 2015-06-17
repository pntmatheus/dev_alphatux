# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20150504_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPolaridade',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'TipoPolaridades',
                'verbose_name': 'TipoPolaridade',
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='ap',
            old_name='numeroSerie',
            new_name='numero_serie',
        ),
        migrations.RenameField(
            model_name='distribuidorinterno',
            old_name='numeroSerie',
            new_name='numero_serie',
        ),
        migrations.AddField(
            model_name='ap',
            name='tipo_polaridade',
            field=models.ForeignKey(to='core.TipoPolaridade', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='tipo_polaridade',
            field=models.ForeignKey(to='core.TipoPolaridade', default=1),
            preserve_default=False,
        ),
    ]
