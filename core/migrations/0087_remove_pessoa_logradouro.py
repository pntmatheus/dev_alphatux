# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_pessoa_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='logradouro',
        ),
    ]
