# Generated by Django 2.1.3 on 2018-11-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('value', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carta',
            name='boost',
            field=models.CharField(choices=[('P', 'Pontos'), ('M', 'Moedas')], default='P', max_length=10, verbose_name='boost_carta'),
        ),
    ]
