# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20150507_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfildeusuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='PerfilDeUsuario',
        ),
    ]
