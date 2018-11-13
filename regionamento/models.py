from django.db import models

# Create your models here.


class Idioma(models.Model):
	nome = models.CharField('nome', max_length=100)
	

class Regiao(models.Model):

	nome = models.CharField('nome', max_length=100)
	


class ConexaoRegiao(models.Model):

	nome = models.CharField('nome', max_length=100)

	reg1 = models.ForeignKey(Regiao, null=False, blank=False, on_delete=models.CASCADE)
	reg2 = models.ForeignKey(Regiao, null=False, blank=False, on_delete=models.CASCADE)

	
