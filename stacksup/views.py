from django.shortcuts import render

from django.views.generic import View
from usuario_perfil.models import UserProfile
from value.models import Carteira

from regionamento.models import Regiao, Idioma

from django.http import HttpResponseRedirect

from .models import Partida, SUQuestionLog


# Create your views here.
class Index(View):

	def get(self, request):

		values = {}

		if request.user.is_authenticated:
			user = UserProfile.objects.filter(nome=request.user) 

			carteira = Carteira.objects.filter(user=request.user).first()



			user = user.first()

		else:
			# user = None
			# carteira = None
			return HttpResponseRedirect("/login")

		values['usuario'] = user
		values['carteira'] = carteira

		return render(
		request,
		'stacksup/index.html',
		context=values,
		)


class NovaPartida(View):

	def get(self, request):

		values = {}

		if request.user.is_authenticated:
			user = UserProfile.objects.filter(nome=request.user).first()

			carteira = Carteira.objects.filter(user=request.user).first()

			idiomas = user.idiomas.all().first()

			id2 = Idioma.objects.all()


			regioes = user.regioes.all().first()
			reg2 = Regiao.objects.all()


		else:
			# user = None
			# carteira = None
			return HttpResponseRedirect("/")

		values['usuario'] = user
		values['carteira'] = carteira

		values['idiomas'] = id2
		values['regioes'] = reg2

		values['idiomaUser'] = idiomas
		values['regiaoUser'] = regioes

		return render(
		request,
		'stacksup/nova_partida.html',
		context=values,
		)

	def post(self, request):

		ESCOLHA_CUSTO_PARTIDA = [0, 100, 500, 1000]


		idioma = request.POST.get('idioma', False)
		regiao = request.POST.get('regiao', False)
		preco = request.POST.get('preco', False)

		if preco == False:
			return HttpResponseRedirect("/")
		


		p = Partida(usuario_partida=request.user, custo=preco)
		

		usuario = models.OneToOneField(User, related_name='usuario_partida', on_delete=models.CASCADE)

	# quando foi criado
	# date = models.DateTimeField('data_criacao', auto_now_add=True, blank=True)

	# # as questoes da partida
	# q1_categoria_1 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_1', on_delete=models.SET_NULL)
	# q1_categoria_2 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_2', on_delete=models.SET_NULL)
	# q1_categoria_3 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_3', on_delete=models.SET_NULL)
	# q1_categoria_4 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_4', on_delete=models.SET_NULL)
	# q1_categoria_5 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_1_categoria_5', on_delete=models.SET_NULL)

	# carteira_se_chegar_aqui_1 = models.ForeignKey(Carteira, related_name='carteira_se_chegar_aqui_1', null=True, blank=False, on_delete=models.SET_NULL)

	# q2_categoria_1 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_1', on_delete=models.SET_NULL)
	# q2_categoria_2 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_2', on_delete=models.SET_NULL)
	# q2_categoria_3 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_3', on_delete=models.SET_NULL)
	# q2_categoria_4 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_4', on_delete=models.SET_NULL)
	# q2_categoria_5 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_2_categoria_5', on_delete=models.SET_NULL)

	# carteira_se_chegar_aqui_2 = models.ForeignKey(Carteira, related_name='carteira_se_chegar_aqui_2', null=True, blank=False, on_delete=models.SET_NULL)

	# q3_categoria_1 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_1', on_delete=models.SET_NULL)
	# q3_categoria_2 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_2', on_delete=models.SET_NULL)
	# q3_categoria_3 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_3', on_delete=models.SET_NULL)
	# q3_categoria_4 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_4', on_delete=models.SET_NULL)
	# q3_categoria_5 = models.OneToOneField(SUQuestionLog, null=True, related_name='questao_3_categoria_5', on_delete=models.SET_NULL)

	# carteira_se_chegar_aqui_3 = models.ForeignKey(Carteira, related_name='carteira_se_chegar_aqui_3', null=True, blank=False, on_delete=models.SET_NULL)


	# # custo para jogar
	# custo = models.IntegerField('custo', default=2)

		return HttpResponseRedirect("/")


class PartidaView(View):

	def get(self, request, id_partida):


		if request.user.is_authenticated:

			partida = Partida.objects.filter(id=id_partida).first()

			# nao tem partida, vai pra 
			if partida == None:
				return HttpResponseRedirect("/nova_partida")
				
		else:
			return HttpResponseRedirect("/")
		
		


		values = {}



		return render(
		request,
		'stacksup/partida.html',
		context=values,
		)
