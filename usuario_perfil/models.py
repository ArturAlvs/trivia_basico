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

	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

	nome = models.CharField('nome', max_length=100)
	age = models.IntegerField('age')
	# telephone = models.CharField('telephone', max_length=15)
	gender = models.CharField('gender', max_length=9, choices=GENDER_CHOICES, default="M")
	# schooling = models.CharField('schooling', max_length=1, choices=SCHOOLING_CHOICES, default="0")
	# course = models.CharField('course', max_length=50)
	# institution = models.CharField('institution', max_length=50)
	# period = models.CharField('period', max_length=20)
	# payed = models.BooleanField('payed', default=False)

	# team = models.ForeignKey(MarathonTeam, null=True, blank=True, on_delete=models.SET_NULL)


	regioes = models.ManyToManyField(Regiao, blank=False, default=None)
	idiomas = models.ManyToManyField(Idioma, blank=False, default=None)


	REQUIRED_FIELDS = ['nome']

	# def __unicode__(self):
	# 	return self.user.username

	# def getFirstName(self):
	# 	return self.nome.split(' ')[0]