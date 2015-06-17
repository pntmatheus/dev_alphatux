# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_auto_20150607_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cep',
            name='ruas',
        ),
        migrations.AddField(
            model_name='cep',
            name='rua',
            field=models.ForeignKey(null=True, to='core.Rua'),
            preserve_default=True,
        ),
    ]
