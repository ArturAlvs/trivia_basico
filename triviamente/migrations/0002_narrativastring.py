# Generated by Django 2.1.3 on 2018-11-16 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regionamento', '0001_initial'),
        ('triviamente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NarrativaString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pergunta_ou_resposta', models.CharField(choices=[('P', 'Pergunta'), ('R', 'Resposta')], max_length=9, verbose_name='tipo')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regionamento.Idioma')),
                ('pergunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pergunta', to='triviamente.Pergunta')),
                ('resposta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resposta', to='triviamente.Resposta')),
                ('user_criador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_criador_narrativa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]