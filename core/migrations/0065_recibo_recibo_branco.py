# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_auto_20150524_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='recibo_branco',
            field=models.FileField(blank=True, editable=False, upload_to='Recibos/'),
            preserve_default=True,
        ),
    ]
