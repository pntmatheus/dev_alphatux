# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_auto_20150508_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='observacoes',
            field=models.TextField(blank=True, default='Serviços de Internet'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recibo',
            name='pessoa',
            field=models.ForeignKey(editable=False, to='core.Pessoa'),
            preserve_default=True,
        ),
    ]
