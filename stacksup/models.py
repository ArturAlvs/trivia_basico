from django.db import models

from django.contrib.auth.models import User

from triviamente.models import Questao, Resposta, NarrativaString

from value.models import Carteira

# stacks up é o nome da modalidade de jogo
# consiste em um conjunto de perguntas e o objetivo é acertar o maximo possivel
# estilo show-do-bilhao, quem quer ser um milhonario


# log da resposta do usuario
# pensar no on_delete de todos!!!!
class SUQuestionLog(models.Model):

	# qual questao foi respondida
	questao = models.ForeignKey(Questao, null=True, blank=False, on_delete=models.CASCADE)

	# qual foi a resposta
	resposta = models.ForeignKey(Resposta, null=True, blank=True, on_delete=models.SET_NULL)


	# quando respondeu
	data_resposta = models.DateTimeField('data_resposta', blank=True, null=True)

	def __str__(self):
		narrativa = str(self.id)
		# try:
		# 	# narrativa = NarrativaString.objects.filter(pergunta=self.questao.pergunta).first()
		# 	q = self.questao.pergunta
		# 	narrativa = NarrativaString.objects.select_related('pergunta').filter(pergunta=q).first()
		# 	narrativa = narrativa.narrativa
		# except Exception as e:
		# 	pass
	
		return narrativa


class Partida(models.Model):

	# adicionar mais
	# CUSTO_ZERO = 1
	# CUSTO_PEQUENO = 2
	# CUSTO_MEDIO = 3
	# CUSTO_GRANDE = 4
	# CUSTO_ENORME = 5
	# CUSTO_ABSURDO = 6
	# ESCOLHA_CUSTO_PARTIDA = (
	# 	(CUSTO_ZERO, "CUSTO_ZERO"),
	# 	(CUSTO_PEQUENO, "CUSTO_PEQUENO"),
	# 	(CUSTO_MEDIO, "CUSTO_MEDIO"),
	# 	(CUSTO_GRANDE, "CUSTO_GRANDE"),
	# 	(CUSTO_ENORME, "CUSTO_ENORME"),
	# 	(CUSTO_ABSURDO, "CUSTO_ABSURDO"),
	# )

	usuario_partida = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

	# quando foi criado
	date = models.DateTimeField('data_criacao', auto_now_add=True, blank=True)

	# as questoes da partida
	q1_categoria_1 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_1', on_delete=models.SET_NULL)
	q1_categoria_2 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_2', on_delete=models.SET_NULL)
	q1_categoria_3 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_3', on_delete=models.SET_NULL)
	q1_categoria_4 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_4', on_delete=models.SET_NULL)
	q1_categoria_5 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_5', on_delete=models.SET_NULL)

	q2_categoria_1 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_1', on_delete=models.SET_NULL)
	q2_categoria_2 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_2', on_delete=models.SET_NULL)
	q2_categoria_3 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_3', on_delete=models.SET_NULL)
	q2_categoria_4 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_4', on_delete=models.SET_NULL)
	q2_categoria_5 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_5', on_delete=models.SET_NULL)

	q3_categoria_1 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_1', on_delete=models.SET_NULL)
	q3_categoria_2 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_2', on_delete=models.SET_NULL)
	q3_categoria_3 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_3', on_delete=models.SET_NULL)
	q3_categoria_4 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_4', on_delete=models.SET_NULL)
	q3_categoria_5 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_5', on_delete=models.SET_NULL)


	# custo para jogar
	custo = models.IntegerField('custo', default=0)

	carteira_de_premiacao = models.ForeignKey(Carteira, related_name='carteira_de_premiacao', null=True, blank=False, on_delete=models.SET_NULL)


	aberta = models.BooleanField(default=True)


