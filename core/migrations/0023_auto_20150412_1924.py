# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20150412_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='ip_acesso',
            field=models.GenericIPAddressField(unpack_ipv4=True),
            preserve_default=True,
        ),
    ]
