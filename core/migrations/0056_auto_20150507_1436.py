# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20150507_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuidorinterno',
            name='cliente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Cliente', null=True),
            preserve_default=True,
        ),
    ]
