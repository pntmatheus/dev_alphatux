# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_pessoa_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('competencia', models.CharField(max_length=50)),
                ('observacoes', models.TextField(blank=True)),
                ('data_emissao', models.DateField(editable=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('recibo_assinado', models.FileField(upload_to='Recibos/', blank=True)),
                ('cliente', models.ForeignKey(to='core.Cliente')),
                ('pessoa', models.ForeignKey(to='core.Pessoa')),
            ],
            options={
                'verbose_name': 'Recibo',
                'verbose_name_plural': 'Recibos',
            },
            bases=(models.Model,),
        ),
    ]
