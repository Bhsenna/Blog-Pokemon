# Generated by Django 4.1 on 2022-09-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0004_alter_pagina_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
