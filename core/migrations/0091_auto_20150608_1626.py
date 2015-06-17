# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0090_auto_20150608_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logradouro',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='logradouro',
            name='rua',
        ),
        migrations.DeleteModel(
            name='Logradouro',
        ),
    ]
