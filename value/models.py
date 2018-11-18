from django.db import models

from django.contrib.auth.models import User


from regionamento.models import Regiao, Idioma




class Carta(models.Model):

	# adicionar mais
	ESCOLHA_BOOST_CARTA = (
		("P", "Pontos"),
		("M", "Moedas"),
	)

	boost = models.CharField('boost_carta', max_length=10, choices=ESCOLHA_BOOST_CARTA, default='P')


	quantidade = models.IntegerField('quantidade')

	nome = models.CharField('nome', max_length=100)


class Album(models.Model):

	user = models.OneToOneField(User, related_name='usuario_album', on_delete=models.CASCADE)

	cartas = models.ManyToManyField(Carta, blank=True, default=None)

	
class Carteira(models.Model):

	# quando a carteira contem de cada
	pontos = models.IntegerField('pontos')
	moedas = models.IntegerField('moedas')

	cartas = models.ManyToManyField(Carta, blank=True, default=None)

	# usuario dono da carteira
	user = models.OneToOneField(User, related_name='usuario_carteira', on_delete=models.CASCADE, null=True)

	# para lembrar que carteira é essa:
	# exemplos:
	# 	usuario_90312
	# 	carteira_padrao_tipo_jogo_1
	# 	carteira_compra_1453
	comentario = models.CharField('comentario', max_length=100)


class Compra(models.Model):

	carteira = models.ForeignKey(Carteira, null=True, blank=False, on_delete=models.SET_NULL)
	user = models.OneToOneField(User, related_name='usuario_compra', on_delete=models.CASCADE, null=False)

	usado = models.BooleanField('usado', default=False)

