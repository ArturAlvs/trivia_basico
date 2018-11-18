# Generated by Django 2.1.3 on 2018-11-17 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triviamente', '0002_narrativastring'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(default='', max_length=300, verbose_name='texto')),
            ],
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='narrativa',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='narrativa',
        ),
        migrations.AddField(
            model_name='narrativastring',
            name='narrativa',
            field=models.CharField(default='', max_length=100, verbose_name='texto'),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='tipo_pergunta_ou_resposta',
            field=models.CharField(choices=[('0', 'Artes'), ('1', 'Ciencias'), ('2', 'Cotidiano'), ('3', 'Esportes'), ('4', 'Geografia'), ('5', 'Historia')], default='0', max_length=20, verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='narrativastring',
            name='tipo_pergunta_ou_resposta',
            field=models.CharField(choices=[('P', 'Pergunta'), ('R', 'Resposta')], default='0', max_length=9, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='opiniaopergunta',
            name='escolha_usuario',
            field=models.CharField(choices=[('0', 'Mal formulada'), ('1', 'Escrita sem significado')], default='0', max_length=10, verbose_name='reclamacao'),
        ),
        migrations.AlterField(
            model_name='opiniaoquestao',
            name='escolha_usuario',
            field=models.CharField(choices=[('0', 'Não existe resposta correta'), ('1', 'Tempo nao suficiente')], default='0', max_length=10, verbose_name='reclamacao'),
        ),
        migrations.AlterField(
            model_name='opiniaoresposta',
            name='escolha_usuario',
            field=models.CharField(choices=[('0', 'Mal formulada'), ('1', 'Escrita sem significado')], default='0', max_length=10, verbose_name='reclamacao'),
        ),
        migrations.AlterField(
            model_name='prototipoquestao',
            name='escolha_usuario',
            field=models.CharField(choices=[('0', 'Ruim'), ('1', 'Neutra'), ('2', 'Boa')], default='0', max_length=10, verbose_name='reclamacao'),
        ),
        migrations.AlterField(
            model_name='questao',
            name='dificuldade',
            field=models.CharField(choices=[('F', 'Facil'), ('D', 'Dificil')], default='0', max_length=9, verbose_name='dificuldade'),
        ),
        migrations.AddField(
            model_name='referencia',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triviamente.Pergunta'),
        ),
        migrations.AddField(
            model_name='resposta',
            name='referencias',
            field=models.ManyToManyField(blank=True, default=None, to='triviamente.Referencia'),
        ),
    ]