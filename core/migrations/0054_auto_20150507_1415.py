# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20150504_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuidorinterno',
            name='cliente',
            field=models.ForeignKey(to='core.Cliente', null=True, on_delete=django.db.models.deletion.SET_NULL),
            preserve_default=True,
        ),
    ]
