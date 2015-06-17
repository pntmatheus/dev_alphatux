# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_auto_20150507_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispositivocliente',
            name='polaridade',
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='ativo',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='numero_serie',
            field=models.CharField(default='', blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='pessoa',
            field=models.ForeignKey(default=1, to='core.Pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Cliente'),
            preserve_default=True,
        ),
    ]
