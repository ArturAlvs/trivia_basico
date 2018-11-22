from django.shortcuts import render

from django.views.generic import View
from usuario_perfil.models import UserProfile
from value.models import Carteira

from triviamente.models import Questao, NarrativaString, Pergunta, Resposta, Referencia


from regionamento.models import Regiao, Idioma, ConexaoRegiao

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
			return HttpResponseRedirect("/nova_partida")


		# checando se usuario pode competir por zero
		if preco == 0 and not UserProfile.objects.filter(nome=request.user).first().premium:
			return HttpResponseRedirect("/nova_partida")

		
		


		p = Partida(usuario=request.user, custo=preco)
		

		# usuario = models.OneToOneField(User, related_name='usuario_partida', on_delete=models.CASCADE)

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


# aqui vao as view de logs, adicionar perguntas e regioes
class FabricaView(View):

	def get(self, request):

		values = {}
		qs = []

		if request.user.is_authenticated:
			user = UserProfile.objects.filter(nome=request.user) 

			carteira = Carteira.objects.filter(user=request.user).first()

			questoes = Questao.objects.filter(user_criador=request.user).order_by('-date')

			try:

				# cada questao criada pelo usuario
				for questao in questoes:

					# a pergunda
					pergunta = NarrativaString.objects.filter(pergunta=questao.pergunta).first()

					# as respostas
					respostas = []
					correta = None
					for resposta in questao.respostas.all():
						
						respostas.append( NarrativaString.objects.filter(resposta=resposta).first() )

						# verificando se a resposta é a correta
						for referencia in resposta.referencias.all():
							if referencia.pergunta == questao.pergunta:
								correta = NarrativaString.objects.filter(resposta=resposta).first()
								
					categoria = questao.pergunta.tipo_pergunta_ou_resposta
					data_criacao = questao.date

					qs.append( (pergunta, respostas, correta, categoria, data_criacao) )



			except Exception as e:
				raise


			regioes = Regiao.objects.all()

			# logs
			logs = []
			partidas = Partida.objects.filter(usuario=request.user)

			try:
				for partida in partidas:
					log.append( partida.q1_categoria_1 )

				values['logs'] = logs

			except Exception as e:
				pass

			user = user.first()

		else:
			# user = None
			# carteira = None
			return HttpResponseRedirect("/login")

		values['usuario'] = user
		values['carteira'] = carteira
		values['questoes'] = qs

		values['regioes'] = regioes


		return render(
		request,
		'stacksup/fabrica.html',
		context=values,
		)


	def post(self, request):


		# dados do user
		user = UserProfile.objects.filter(nome=request.user).first()
		
		idioma = user.idiomas.all().first()
		reg = user.regioes.all().first()

		# dados das questoes
		textoPerguntaQuestao = request.POST.get('textoPerguntaQuestao', False)
		textoRespostaCorreta = request.POST.get('textoRespostaCorreta', False)
	
		# dados da regiao
		nomeDaRegiao = request.POST.get('nomeDaRegiao', False)


		# receber o tipo do usuario
		if textoPerguntaQuestao != False and textoRespostaCorreta != False:

			regiao_da_questao = request.POST.get('regiaoFormControlSelectQuestao', False)

			regiao_pergunta = Regiao.objects.filter(name=regiao_da_questao).first()


			textoRespostaErrada1 = request.POST.get('textoRespostaErrada1', False)
			textoRespostaErrada2 = request.POST.get('textoRespostaErrada2', False)
			textoRespostaErrada3 = request.POST.get('textoRespostaErrada3', False)

			categoria = request.POST.get('categoriaFormControlSelect', False)

			try:

				pergunta = None
				if categoria == "Artes":
					pergunta = Pergunta(tipo_pergunta_ou_resposta=0)
					pergunta.save()	
									
				elif categoria == "Ciencias":
					pergunta = Pergunta(tipo_pergunta_ou_resposta=1)
					pergunta.save()
					
				elif categoria == "Cotidiano":

					pergunta = Pergunta(tipo_pergunta_ou_resposta=2)
					pergunta.save()
					
				elif categoria == "Esportes":

					pergunta = Pergunta(tipo_pergunta_ou_resposta=3)
					pergunta.save()
					
				elif categoria == "Geografia":
					pergunta = Pergunta(tipo_pergunta_ou_resposta=4)
					pergunta.save()
					
				elif categoria == "Historia":
					pergunta = Pergunta(tipo_pergunta_ou_resposta=5)
					pergunta.save()
					

	# ("0", "Artes"),
	# 		("1", "Ciencias"),
	# 		("2", "Cotidiano"),
	# 		("3", "Esportes"),
	# 		("4", "Geografia"),
	# 		("5", "Historia"),


				refe = Referencia(pergunta=pergunta, texto=request.user)
				refe.save()

				respostaCorreta = Resposta()
				respostaCorreta.save()
				respostaCorreta.referencias.add(refe)

				respostaErrada1 = Resposta()
				respostaErrada1.save()

				respostaErrada2 = Resposta()
				respostaErrada2.save()

				respostaErrada3 = Resposta()
				respostaErrada3.save()

				narrativaPergunta = NarrativaString(tipo_pergunta_ou_resposta="P", idioma=idioma, user_criador=request.user, narrativa=textoPerguntaQuestao, pergunta=pergunta)
				narrativaPergunta.save()

				narrativaRespostaCorreta = NarrativaString(tipo_pergunta_ou_resposta="R", idioma=idioma, user_criador=request.user, narrativa=textoRespostaCorreta, resposta=respostaCorreta)
				narrativaRespostaCorreta.save()
				narrativaRespostaErrada1 = NarrativaString(tipo_pergunta_ou_resposta="R", idioma=idioma, user_criador=request.user, narrativa=textoRespostaErrada1, resposta=respostaErrada1)
				narrativaRespostaErrada1.save()
				narrativaRespostaErrada2 = NarrativaString(tipo_pergunta_ou_resposta="R", idioma=idioma, user_criador=request.user, narrativa=textoRespostaErrada2, resposta=respostaErrada2)
				narrativaRespostaErrada2.save()
				narrativaRespostaErrada3 = NarrativaString(tipo_pergunta_ou_resposta="R", idioma=idioma, user_criador=request.user, narrativa=textoRespostaErrada3, resposta=respostaErrada3)
				narrativaRespostaErrada3.save()


				questao = Questao(user_criador=request.user, pergunta=pergunta, regiao=regiao_pergunta)
				questao.save()
				questao.respostas.add(respostaCorreta)
				questao.respostas.add(respostaErrada1)
				questao.respostas.add(respostaErrada2)
				questao.respostas.add(respostaErrada3)

			except Exception as e:
				raise


		elif nomeDaRegiao != False:

			

			regiao_pai_nome = request.POST.get('regiaoFormControlSelect', False)
			
			try:
				regiao = Regiao(nome=nomeDaRegiao)

				regiao_pai = Regiao.objects.filter(nome=regiao_pai_nome).first()

				regiao.save()
				criado_por = "Criado por: " + str(request.user)
				conexao = ConexaoRegiao(nome=criado_por, reg1=regiao_pai ,reg2=regiao)

				conexao.save()
			
			except Exception as e:
				raise

		else:
			return HttpResponseRedirect("/fabrica")


		
		return HttpResponseRedirect("/fabrica")
		



		
		
