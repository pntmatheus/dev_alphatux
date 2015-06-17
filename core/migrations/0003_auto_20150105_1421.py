# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20141230_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilDeUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('perfil', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='usuario_do_sistema')),
            ],
            options={
                'verbose_name': 'Perfil de Usuário',
                'verbose_name_plural': 'Perfis de Usuário',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usuariosistema',
            name='user',
        ),
        migrations.DeleteModel(
            name='UsuarioSistema',
        ),
    ]
