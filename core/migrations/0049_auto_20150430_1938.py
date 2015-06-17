# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20150430_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pessoa',
            field=models.OneToOneField(default=2, to='core.Pessoa'),
            preserve_default=True,
        ),
    ]
