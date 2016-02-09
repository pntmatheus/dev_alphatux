# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20160131_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivocliente',
            name='ip_acesso',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='endereco',
            field=models.ForeignKey(verbose_name='Endereço de Instalação', to='core.Endereco', null=True),
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='mac_wan',
            field=models.CharField(verbose_name='MAC da WAN', max_length=17),
        ),
        migrations.AlterField(
            model_name='dispositivocliente',
            name='pessoa',
            field=models.ForeignKey(verbose_name='Dono do Aparelho', to='core.Pessoa'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(blank=True, verbose_name='Data Nascimento/ Abertura', null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(verbose_name='Nome Completo', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone1',
            field=models.CharField(verbose_name='Telefone Principal', max_length=14),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone2',
            field=models.CharField(blank=True, verbose_name='Outro Telefone', max_length=14),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='tipo_pessoa',
            field=models.ForeignKey(to='core.TipoPessoa', default=1),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(verbose_name='Usuário', to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
