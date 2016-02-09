# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20160209_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterUniqueTogether(
            name='endereco',
            unique_together=set([('cep', 'numero')]),
        ),
    ]
