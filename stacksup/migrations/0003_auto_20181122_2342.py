# Generated by Django 2.1.3 on 2018-11-22 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('value', '0004_auto_20181122_1328'),
        ('stacksup', '0002_auto_20181121_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='carteira_se_chegar_aqui_1',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='carteira_se_chegar_aqui_2',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='carteira_se_chegar_aqui_3',
        ),
        migrations.AddField(
            model_name='partida',
            name='carteira_de_premiacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carteira_de_premiacao', to='value.Carteira'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='custo',
            field=models.IntegerField(default=0, verbose_name='custo'),
        ),
    ]