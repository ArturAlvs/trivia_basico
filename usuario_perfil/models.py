from django.db import models

from django.contrib.auth.models import User

from regionamento.models import Regiao, Idioma



# class MarathonTeam(models.Model):

#     nick = models.CharField('nick', max_length=30)


class UserProfile(models.Model):

	# adicionar mais
	GENDER_CHOICES = (
		("M", "Masculino"),
		("F", "Feminino"),
	)

	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)

	nome = models.CharField('nome', max_length=100)
	age = models.IntegerField('age')
	gender = models.CharField('gender', max_length=9, choices=GENDER_CHOICES, default="M")

	regioes = models.ManyToManyField(Regiao, blank=True, default=None)
	idiomas = models.ManyToManyField(Idioma, blank=True, default=None)


	REQUIRED_FIELDS = ['nome']

	def __str__(self):
		return self.nome + " ; " + self.user.email

	# def __unicode__(self):
	# 	return self.user.username

	# def getFirstName(self):
	# 	return self.nome.split(' ')[0]