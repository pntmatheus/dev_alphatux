# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_auto_20150507_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivocliente',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.Cliente'),
            preserve_default=True,
        ),
    ]
