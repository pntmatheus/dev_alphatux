# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160202_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivocliente',
            name='ap',
            field=models.ForeignKey(verbose_name='AP', to='core.AP'),
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='ip_acesso',
            field=models.CharField(max_length=50, blank=True, verbose_name='IP de Acesso', null=True),
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='tipo_polaridade',
            field=models.ForeignKey(verbose_name='Polaridade Instalada', to='core.TipoPolaridade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(max_length=10, unique=True, default=''),
        ),
    ]
