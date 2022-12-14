# Generated by Django 4.1 on 2022-09-08 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('conteude', models.TextField()),
                ('descricao', models.TextField(blank=True)),
                ('titulo', models.CharField(max_length=20)),
                ('imagem', models.CharField(max_length=15)),
                ('autor', models.CharField(max_length=20)),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='geral.categoria')),
            ],
        ),
    ]
