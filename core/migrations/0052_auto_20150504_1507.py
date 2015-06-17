# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20150504_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribuidorinterno',
            name='logradouro',
            field=models.ForeignKey(default=1, to='core.Logradouro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='numeroSerie',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='pessoa',
            field=models.ForeignKey(default=1, to='core.Pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='distribuidorinterno',
            name='cliente',
            field=models.ForeignKey(null=True, to='core.Cliente'),
            preserve_default=True,
        ),
    ]
