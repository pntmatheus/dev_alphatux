# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0092_auto_20150608_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='arquivo_conf',
            field=models.FileField(upload_to='APs/arquivos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ap',
            name='foto_ap',
            field=models.ImageField(upload_to='APs/fotos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='pessoa',
            field=models.ForeignKey(to='core.Pessoa', verbose_name='dono'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='vencimento',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='distribuidorinterno',
            name='pessoa',
            field=models.ForeignKey(to='core.Pessoa', verbose_name='dono'),
            preserve_default=True,
        ),
    ]
