# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150128_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='pop',
            name='foto_pop',
            field=models.ImageField(upload_to='POPs/fotos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pop',
            name='logradouro',
            field=models.OneToOneField(to='core.Logradouro', default=''),
            preserve_default=False,
        ),
    ]
