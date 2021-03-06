# Generated by Django 2.1.3 on 2018-11-16 05:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MSG_SYST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('P', 'Presente'), ('A', 'Alerta'), ('C', 'Compra')], default='A', max_length=9, verbose_name='gender')),
                ('texto', models.CharField(max_length=500, verbose_name='nome')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='data_criacao_mensagem')),
                ('user', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
