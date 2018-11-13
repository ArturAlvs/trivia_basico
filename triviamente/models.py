from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pergunta(models.Model):

	user_criador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

	texto_pergunta = models.CharField('texto_pergunta', max_length=100)


class Resposta(models.Model):

	user_criador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

	texto_resposta = models.CharField('texto_resposta', max_length=100)


class Questao(models.Model):

	user_criador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

	pergunta = models.ForeignKey(Pergunta, null=True, blank=True, on_delete=models.SET_NULL)

	resp1 = models.ForeignKey(Resposta, null=True, blank=True, on_delete=models.SET_NULL)
	resp2 = models.ForeignKey(Resposta, null=True, blank=True, on_delete=models.SET_NULL)
	resp3 = models.ForeignKey(Resposta, null=True, blank=True, on_delete=models.SET_NULL)
	resp4 = models.ForeignKey(Resposta, null=True, blank=True, on_delete=models.SET_NULL)

	# REQUIRED_FIELDS = ['nome']

	def __unicode__(self):
		return self.user.username

	def getFirstName(self):
		return self.nome.split(' ')[0]


