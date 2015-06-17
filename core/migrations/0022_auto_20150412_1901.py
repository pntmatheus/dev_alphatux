# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150129_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='firmware',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ap',
            name='ip_acesso',
            field=models.GenericIPAddressField(),
            preserve_default=True,
        ),
    ]
