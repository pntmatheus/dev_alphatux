# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_remove_cliente_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cliente_desde',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
