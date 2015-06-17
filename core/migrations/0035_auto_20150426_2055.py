# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='logradouro',
            field=models.ForeignKey(to='core.Logradouro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='pessoa_fisica',
            field=models.OneToOneField(null=True, blank=True, to='core.PessoaFisica'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='pessoa_juridica',
            field=models.OneToOneField(null=True, blank=True, to='core.PessoaJuridica'),
            preserve_default=True,
        ),
    ]
