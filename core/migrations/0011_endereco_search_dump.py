# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160209_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='search_dump',
            field=models.CharField(blank=True, default='', max_length=255, editable=False),
        ),
    ]
