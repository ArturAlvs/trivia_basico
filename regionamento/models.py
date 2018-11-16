from django.db import models
from django.contrib.auth.models import User



class Idioma(models.Model):
	nome = models.CharField('nome', max_length=100)
	

class Regiao(models.Model):

	nome = models.CharField('nome', max_length=100)
	


class ConexaoRegiao(models.Model):

	nome = models.CharField('nome', max_length=100)

	# reg1 é pai de reg2
	reg1 = models.ForeignKey(Regiao, related_name='regiao_pai', null=False, blank=False, on_delete=models.CASCADE)
	reg2 = models.ForeignKey(Regiao, related_name='regiao_filho', null=False, blank=False, on_delete=models.CASCADE)

	
class OpiniaoRegiao(models.Model):
	ESCOLHA_OPINIAO_REGIAO = (
		("0", "Ruim"),
		("1", "Neutra"),
		("2", "Boa"),
	)

	# tem que ser models.CASCADE se quando a pergunta for deletada, o log de reclamacao de pergunta do user tambem é
	regiao = models.ForeignKey(Regiao, null=True, blank=False, on_delete=models.SET_NULL)

	user_criador = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
	# o que o jogador escolheu
	escolha_usuario = models.CharField('opiniao_regiao', choices=ESCOLHA_OPINIAO_REGIAO, max_length=10)

class OpiniaoConexao(models.Model):
	ESCOLHA_OPINIAO_CONEXAO_REGIAO = (
		("0", "Ruim"),
		("1", "Neutra"),
		("2", "Boa"),
	)

	# tem que ser models.CASCADE se quando a pergunta for deletada, o log de reclamacao de pergunta do user tambem é
	conexao_regiao = models.ForeignKey(ConexaoRegiao, null=True, blank=False, on_delete=models.SET_NULL)

	user_criador = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
	# o que o jogador escolheu
	escolha_usuario = models.CharField('opiniao_conexao_regiao', choices=ESCOLHA_OPINIAO_CONEXAO_REGIAO, max_length=10)
