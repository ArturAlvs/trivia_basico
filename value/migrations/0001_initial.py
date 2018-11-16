# Generated by Django 2.1.3 on 2018-11-16 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='quantidade')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField(verbose_name='pontos')),
                ('moedas', models.IntegerField(verbose_name='moedas')),
                ('comentario', models.CharField(max_length=100, verbose_name='comentario')),
                ('cartas', models.ManyToManyField(blank=True, default=None, to='value.Carta')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_carteira', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usado', models.BooleanField(default=False, verbose_name='usado')),
                ('carteira', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='value.Carteira')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_compra', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='cartas',
            field=models.ManyToManyField(blank=True, default=None, to='value.Carta'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_album', to=settings.AUTH_USER_MODEL),
        ),
    ]