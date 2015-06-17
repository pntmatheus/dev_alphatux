# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150126_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='arquivo_conf',
            field=models.FileField(upload_to='APs/arquivos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ap',
            name='foto_ap',
            field=models.ImageField(upload_to='APs/fotos'),
            preserve_default=True,
        ),
    ]
