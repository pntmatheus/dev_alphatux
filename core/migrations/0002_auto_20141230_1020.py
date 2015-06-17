# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariosistema',
            name='login',
        ),
        migrations.RemoveField(
            model_name='usuariosistema',
            name='senha',
        ),
        migrations.AddField(
            model_name='usuariosistema',
            name='user',
            field=models.OneToOneField(default=2, to=settings.AUTH_USER_MODEL, related_name='usuario_do_sistema'),
            preserve_default=False,
        ),
    ]
