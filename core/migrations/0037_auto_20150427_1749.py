# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20150427_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoafisica',
            name='apelido',
        ),
        migrations.RemoveField(
            model_name='pessoafisica',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='pessoafisica',
            name='nome',
        ),
    ]
