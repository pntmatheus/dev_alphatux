# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_remove_plano_disposito_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispositivocliente',
            old_name='endereco_mac',
            new_name='mac_wan',
        ),
        migrations.RemoveField(
            model_name='dispositivocliente',
            name='foto_dispositivo_cliente',
        ),
        migrations.RemoveField(
            model_name='dispositivocliente',
            name='situacao',
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='arquivo_conf',
            field=models.FileField(upload_to='APs/arquivos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='firmware',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='foto_instalacao',
            field=models.ImageField(upload_to='DispositivoCliente/fotos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='logradouro',
            field=models.ForeignKey(default='', to='core.Logradouro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='plano',
            field=models.ForeignKey(default='', to='core.Plano'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='polaridade',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='senha',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispositivocliente',
            name='usuario',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
