# Generated by Django 2.1.3 on 2018-11-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stacksup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suquestionlog',
            name='carteira',
        ),
        migrations.AlterField(
            model_name='partida',
            name='custo',
            field=models.IntegerField(default=2, verbose_name='custo'),
        ),
    ]
