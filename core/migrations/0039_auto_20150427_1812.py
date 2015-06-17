# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20150427_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='pessoa_fisica',
            field=models.OneToOneField(to='core.PessoaFisica', blank=True, null=True),
            preserve_default=True,
        ),
    ]
