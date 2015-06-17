# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_recibo_recibo_branco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='competencia',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recibo',
            name='recibo_assinado',
            field=models.FileField(blank=True, upload_to=core.models.content_file_name),
            preserve_default=True,
        ),
    ]
