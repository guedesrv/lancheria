# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do Responsável')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='E-mail')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua')),
                ('region', models.IntegerField(choices=[(1, 'Curitiba'), (2, 'Região Metropolitana')], default=1, verbose_name='Cidade')),
                ('district', models.IntegerField(choices=[(1, 'Ahu'), (2, 'Alto da Glória'), (3, 'Alto da XV'), (4, 'Bacacheri'), (5, 'Batel'), (6, 'Bigorrilho'), (7, 'Boa Vista'), (8, 'Bom Retiro'), (9, 'Cabral'), (10, 'Centro'), (11, 'Centro Cívico'), (12, 'Hugo Lange'), (13, 'Jardim Social'), (14, 'Juvevê'), (15, 'Mercês')], default=1, verbose_name='Bairro')),
                ('number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('plan', models.IntegerField(blank=True, choices=[(1, 'Mensal'), (2, 'Trimestral'), (3, 'Semestral'), (4, 'Mensal (3 x na semana)'), (5, 'Trimestral (3 x na semana)'), (6, 'Semestral (3 x na semana)')], default=1, null=True, verbose_name='Plano')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
