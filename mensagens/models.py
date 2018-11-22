from django.db import models


from django.contrib.auth.models import User


# criar classes parar as mensagens de jogos diferente?



# mensagens do sistema
# pode mandar mensagem de qualquer coisa para o usuario
class MSG_SYST(models.Model):

	# adicionar mais
	TIPOS_MENSAGENS = (
		("P", "Presente"),
		("A", "Alerta"),
		("C", "Compra"),
	)

	tipo_mensagem = models.CharField('tipo_mensagem', max_length=9, choices=TIPOS_MENSAGENS, default="A")

	user = models.ManyToManyField(User, blank=True, default=None)
	texto = models.CharField('nome', max_length=500, default='')
	

	date = models.DateTimeField('data_criacao_mensagem', auto_now_add=True, blank=True)

	def __str__(self):
		return self.texto


class MSG_PARA_SYST(models.Model):

	# adicionar mais
	TIPOS_MENSAGENS = (
		("S", "Sugestão"),
		("R", "Reclamação"),
		("O", "Outros"),
	)

	tipo_mensagem = models.CharField('tipo_mensagem', max_length=9, choices=TIPOS_MENSAGENS, default="S")

	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	texto = models.CharField('nome', max_length=500, default='')
	

	date = models.DateTimeField('data_criacao_mensagem', auto_now_add=True, blank=True)

	def __str__(self):
		return self.texto