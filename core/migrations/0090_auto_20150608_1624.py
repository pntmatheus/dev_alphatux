# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_auto_20150608_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispositivocliente',
            name='logradouro',
        ),
        migrations.RemoveField(
            model_name='distribuidorinterno',
            name='logradouro',
        ),
        migrations.RemoveField(
            model_name='pop',
            name='logradouro',
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='endereco',
            field=models.ForeignKey(null=True, to='core.Endereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distribuidorinterno',
            name='endereco',
            field=models.ForeignKey(null=True, to='core.Endereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pop',
            name='endereco',
            field=models.ForeignKey(null=True, to='core.Endereco'),
            preserve_default=True,
        ),
    ]
