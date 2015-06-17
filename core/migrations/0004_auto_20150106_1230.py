# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150105_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distribuidorinterno',
            options={'verbose_name': 'Distribuidor interno', 'verbose_name_plural': 'Distribuidores internos'},
        ),
        migrations.AlterModelOptions(
            name='perfildeusuario',
            options={'verbose_name': 'Perfil de usuário', 'verbose_name_plural': 'Perfis de usuários'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pop',
            field=models.ForeignKey(to='core.Pop', related_name='clientes', verbose_name='pop'),
            preserve_default=True,
        ),
    ]
