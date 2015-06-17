# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0085_auto_20150607_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.ForeignKey(null=True, to='core.Endereco'),
            preserve_default=True,
        ),
    ]
