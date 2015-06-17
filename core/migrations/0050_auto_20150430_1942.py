# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20150430_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pessoa',
            field=models.OneToOneField(to='core.Pessoa'),
            preserve_default=True,
        ),
    ]
