# Generated by Django 4.2.6 on 2023-11-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livromodel',
            name='ano',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='livromodel',
            name='autor',
            field=models.CharField(max_length=200, null=True, verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='livromodel',
            name='data_alteracao',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data de Alteração'),
        ),
        migrations.AddField(
            model_name='livromodel',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Cadastro'),
        ),
        migrations.AddField(
            model_name='livromodel',
            name='isbn',
            field=models.CharField(max_length=200, null=True, verbose_name='ISBN'),
        ),
        migrations.AddField(
            model_name='livromodel',
            name='numero_paginas',
            field=models.IntegerField(default=1, verbose_name='Número de Páginas'),
        ),
    ]