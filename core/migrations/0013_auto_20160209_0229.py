# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160209_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cep',
            name='codigo',
            field=models.CharField(verbose_name='CEP', max_length=9),
        ),
    ]
