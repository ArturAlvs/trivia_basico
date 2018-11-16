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

	gender = models.CharField('gender', max_length=9, choices=TIPOS_MENSAGENS, default="A")

	user = models.ManyToManyField(User, blank=True, default=None)
	texto = models.CharField('nome', max_length=500)
	

	date = models.DateTimeField('data_criacao_mensagem', auto_now_add=True, blank=True)

	