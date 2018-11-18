from django.db import models
from django.contrib.auth.models import User
from regionamento.models import Regiao, Idioma





class Pergunta(models.Model):

	ESCOLHA_TIPO_AREA = (
		("0", "Artes"),
		("1", "Ciencias"),
		("2", "Cotidiano"),
		("3", "Esportes"),
		("4", "Geografia"),
		("5", "Historia"),
	)

	tipo_pergunta_ou_resposta = models.CharField('categoria', max_length=20, choices=ESCOLHA_TIPO_AREA, default='0')


	def __str__(self):
		narra = NarrativaString.objects.filter(pergunta=self)
		return narra.first().narrativa




class Referencia(models.Model):

	# pergunta que a resposta correta possui a seguinte referencia
	pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

	# link da referencia
	texto = models.CharField('texto', max_length=300, default='')

class Resposta(models.Model):

	referencias = models.ManyToManyField(Referencia, blank=True, default=None)

	def __str__(self):
		narra = NarrativaString.objects.filter(resposta=self)
		return narra.first().narrativa



# narrativa se comporata como uma string que tem um tipo, pergunta ou resposta.
# um conjunto que existe aqui é o Questao, que é uma narrativa composta de duas narrativas, uma que questiona algo e outra que responde com uma verdade
class NarrativaString(models.Model):

	ESCOLHA_TIPO_NARRATIVA = (
		("P", "Pergunta"),
		("R", "Resposta"),	
	)

	tipo_pergunta_ou_resposta = models.CharField('tipo', max_length=9, choices=ESCOLHA_TIPO_NARRATIVA, default='0')

	pergunta = models.ForeignKey(Pergunta, related_name='pergunta', null=True, blank=True, on_delete=models.SET_NULL)
	resposta = models.ForeignKey(Resposta, related_name='resposta', null=True, blank=True, on_delete=models.SET_NULL)

	user_criador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

	# quando deletar um idoma, toda narrativa daquele idioma deveria ser deletado?
	idioma = models.ForeignKey(Idioma, null=True, blank=False, on_delete=models.SET_NULL)

	# string
	narrativa = models.CharField('texto', max_length=100, default='')

	def __str__(self):
		return self.narrativa


# Questao generica, para ser usada por cada jogo
class Questao(models.Model):

	ESCOLHA_DIFICULDADE = (
		("F", "Facil"),
		("D", "Dificil"),	
	)

	# Escolhido de inicio mas muda de 15 em 15 dias de acordo com os acertos
	dificuldade = models.CharField('dificuldade', max_length=9, choices=ESCOLHA_DIFICULDADE, default='0')


	user_criador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

	# tem que ter uma pergunta, pois Questao é a sinapse
	# dependendo do idioma do usuario, tenho que achar a pergunta com o mesmo idioma
	pergunta = models.ForeignKey(Pergunta, null=False, blank=False, on_delete=models.CASCADE)

	# resposta certa é a primeira
	# dependendo do idioma do usuario, tenho que achar as respostas com o mesmo idioma
	respostas = models.ManyToManyField(Resposta, blank=True, default=None)

	# regiao pai
	regiao = models.ForeignKey(Regiao, null=True, blank=True, on_delete=models.SET_NULL)

	# quando foi criada
	date = models.DateTimeField('data_criacao', auto_now_add=True, blank=True)
		 


	def __str__(self):
		texto = NarrativaString.objects.filter(pergunta = self.pergunta)
		return texto.first().narrativa


	# REQUIRED_FIELDS = ['nome']


# log aqui ou em cada app?
# se usuario acertou ou errou.
# class LogQuestaoRespondiaUsuario(models.Model):

# 	ESCOLHA_RESPOSTA_USUARIO = (
# 		("0", "resp1"),
# 		("1", "resp2"),
# 		("2", "resp3"),
# 		("3", "resp4"),
# 	)

# 	# tem que ser models.CASCADE se quando a questao for deletada, o log de pontuação do user tambem é
# 	questao = models.ForeignKey(Questao, null=True, blank=True, on_delete=models.SET_NULL)

# 	user_jogador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)


# 	# o que o jogador escolheu
# 	escolha_usuario = models.CharField('escolha', max_length=9, choices=ESCOLHA_RESPOSTA_USUARIO)

class PrototipoQuestao(models.Model):
	
	ESCOLHA_PROTOTIPO_QUESTAO = (
		("0", "Ruim"),
		("1", "Neutra"),
		("2", "Boa"),
	)

	questao = models.OneToOneField(Questao, on_delete=models.CASCADE, primary_key=True, null=False)

	user_criador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

	escolha_usuario = models.CharField('reclamacao', max_length=10, choices=ESCOLHA_PROTOTIPO_QUESTAO, default='0')

	date = models.DateTimeField('data_criacao', auto_now_add=True, blank=True)





class OpiniaoQuestao(models.Model):

	ESCOLHA_RECLAMACAO_QUESTAO = (
		("0", "Não existe resposta correta"),
		("1", "Tempo nao suficiente"),
	)


	# tem que ser models.CASCADE se quando a questao for deletada, o log de reclamacao de questao do user tambem é
	questao = models.ForeignKey(Questao, null=True, blank=False, on_delete=models.SET_NULL)

	user_criador = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)

	# o que o jogador escolheu
	escolha_usuario = models.CharField('reclamacao', max_length=10, choices=ESCOLHA_RECLAMACAO_QUESTAO, default='0')

	date = models.DateTimeField('data_criacao_opiniao', auto_now_add=True, blank=True)



class OpiniaoPergunta(models.Model):

	ESCOLHA_RECLAMACAO_PERGUNTA = (
		("0", "Mal formulada"),
		("1", "Escrita sem significado"),
	)


	# tem que ser models.CASCADE se quando a pergunta for deletada, o log de reclamacao de pergunta do user tambem é
	pergunta = models.ForeignKey(Pergunta, null=True, blank=False, on_delete=models.SET_NULL)

	user_criador = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)

	# o que o jogador escolheu
	escolha_usuario = models.CharField('reclamacao', max_length=10, choices=ESCOLHA_RECLAMACAO_PERGUNTA, default='0')

	date = models.DateTimeField('data_criacao_opiniao', auto_now_add=True, blank=True)



class OpiniaoResposta(models.Model):

	ESCOLHA_RECLAMACAO_RESPOSTA = (
		("0", "Mal formulada"),
		("1", "Escrita sem significado"),
	)


	# tem que ser models.CASCADE se quando a pergunta for deletada, o log de reclamacao de pergunta do user tambem é
	resposta = models.ForeignKey(Resposta, null=True, blank=False, on_delete=models.SET_NULL)

	user_criador = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)

	# o que o jogador escolheu
	escolha_usuario = models.CharField('reclamacao', max_length=10, choices=ESCOLHA_RECLAMACAO_RESPOSTA, default='0')


	date = models.DateTimeField('data_criacao_opiniao', auto_now_add=True, blank=True)



