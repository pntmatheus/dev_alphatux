# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_tipopessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('telefone1', models.CharField(max_length=20)),
                ('telefone2', models.CharField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('observacoes', models.TextField(blank=True)),
                ('logradouro', models.OneToOneField(to='core.Logradouro')),
                ('pessoa_fisica', models.ForeignKey(null=True, blank=True, to='core.PessoaFisica')),
                ('pessoa_juridica', models.ForeignKey(null=True, blank=True, to='core.PessoaJuridica')),
                ('tipo_pessoa', models.ForeignKey(to='core.TipoPessoa')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
            bases=(models.Model,),
        ),
    ]
