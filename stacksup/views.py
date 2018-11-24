from django.shortcuts import render

from django.views.generic import View
from usuario_perfil.models import UserProfile
from value.models import Carteira

from triviamente.models import Questao, NarrativaString, Pergunta, Resposta, Referencia, PrototipoQuestao


from regionamento.models import Regiao, Idioma, ConexaoRegiao

from django.http import HttpResponseRedirect

from .models import Partida, SUQuestionLog

from random import randint, shuffle

# mudar todos os auto_now_add 
# timezone.now
from django.utils import timezone

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

		ESCOLHA_CUSTO_PARTIDA = [0, 100, 500, 1000, 5000, 10000]


		idioma = request.POST.get('idioma', False)
		regiao = request.POST.get('regiao', False)
		preco = request.POST.get('preco', False)
		preco = int(preco)
		preco_final = preco

		if preco == False:
			return HttpResponseRedirect("/nova_partida")


		# checando se usuario pode competir por zero
		if UserProfile.objects.filter(nome=request.user).first().premium:
			preco_final = 0
		else:
			usuario_perder_moedas = Carteira.objects.filter(user=request.user).first()
			usuario_perder_moedas.moedas = int(usuario_perder_moedas.moedas) - preco_final
			usuario_perder_moedas.save()
		
		carteira_para_a_partida = Carteira.objects.filter(moedas=(preco/2), user=None).first()

		# se não existir, ciro
		if carteira_para_a_partida == None:
			comentario_carteira = "carteira_sistema_"+ str((preco/2)) +"_moedas"
			carteira_para_a_partida = Carteira(moedas=(preco/2), comentario=comentario_carteira )
			carteira_para_a_partida.save()
		

		questoes_escolhidas_p_partida = []
		perguntas_escolhidas_p_partida = []
		categorias_existentes = ["Artes", "Ciencias", "Cotidiano", "Esportes", "Geografia", "Historia"]
		for questao_grupo in range(3):
			
			categorias_questoes = []
			
			for questao_id in range(5):
				# escolho a categoria
				categoria_questao = randint(0, 5)
				while categoria_questao in categorias_questoes:
					categoria_questao = randint(0, 5)

				# adiciona para nao escoler mais
				categorias_questoes.append(categoria_questao)


				pergunta = Pergunta.objects.filter(tipo_pergunta_ou_resposta=categoria_questao).all()

				qual_pergunta = randint(0, (len(pergunta)-1))
				qual_pergunta = pergunta[qual_pergunta]

				while qual_pergunta in perguntas_escolhidas_p_partida:
					qual_pergunta = randint(0, (len(pergunta)-1))
					qual_pergunta = pergunta[qual_pergunta]
				perguntas_escolhidas_p_partida.append(qual_pergunta)


		for perg_p_partida in perguntas_escolhidas_p_partida:
			questoes = Questao.objects.filter(pergunta=perg_p_partida).all()
			qual_questao = randint(0, (len(questoes)-1))
			qual_questao = questoes[qual_questao]
			questoes_escolhidas_p_partida.append(qual_questao)



		q1_categoria_1 = SUQuestionLog(questao=questoes_escolhidas_p_partida[0])
		q1_categoria_1.save()
		q1_categoria_2 = SUQuestionLog(questao=questoes_escolhidas_p_partida[1])
		q1_categoria_2.save()
		q1_categoria_3 = SUQuestionLog(questao=questoes_escolhidas_p_partida[2])
		q1_categoria_3.save()
		q1_categoria_4 = SUQuestionLog(questao=questoes_escolhidas_p_partida[3])
		q1_categoria_4.save()
		q1_categoria_5 = SUQuestionLog(questao=questoes_escolhidas_p_partida[4])
		q1_categoria_5.save()
		q2_categoria_1 = SUQuestionLog(questao=questoes_escolhidas_p_partida[5])
		q2_categoria_1.save()
		q2_categoria_2 = SUQuestionLog(questao=questoes_escolhidas_p_partida[6])
		q2_categoria_2.save()
		q2_categoria_3 = SUQuestionLog(questao=questoes_escolhidas_p_partida[7])
		q2_categoria_3.save()
		q2_categoria_4 = SUQuestionLog(questao=questoes_escolhidas_p_partida[8])
		q2_categoria_4.save()
		q2_categoria_5 = SUQuestionLog(questao=questoes_escolhidas_p_partida[9])
		q2_categoria_5.save()
		q3_categoria_1 = SUQuestionLog(questao=questoes_escolhidas_p_partida[10])
		q3_categoria_1.save()
		q3_categoria_2 = SUQuestionLog(questao=questoes_escolhidas_p_partida[11])
		q3_categoria_2.save()
		q3_categoria_3 = SUQuestionLog(questao=questoes_escolhidas_p_partida[12])
		q3_categoria_3.save()
		q3_categoria_4 = SUQuestionLog(questao=questoes_escolhidas_p_partida[13])
		q3_categoria_4.save()
		q3_categoria_5 = SUQuestionLog(questao=questoes_escolhidas_p_partida[14])
		q3_categoria_5.save()

		partida = Partida(usuario_partida=request.user, custo=preco_final, carteira_de_premiacao=carteira_para_a_partida,
			q1_categoria_1=q1_categoria_1,
			q1_categoria_2=q1_categoria_2,
			q1_categoria_3=q1_categoria_3,
			q1_categoria_4=q1_categoria_4,
			q1_categoria_5=q1_categoria_5,
			q2_categoria_1=q2_categoria_1,
			q2_categoria_2=q2_categoria_2,
			q2_categoria_3=q2_categoria_3,
			q2_categoria_4=q2_categoria_4,
			q2_categoria_5=q2_categoria_5,
			q3_categoria_1=q3_categoria_1,
			q3_categoria_2=q3_categoria_2,
			q3_categoria_3=q3_categoria_3,
			q3_categoria_4=q3_categoria_4,
			q3_categoria_5=q3_categoria_5
			)
		partida.save()

		url_to_go = "/partida/" + str(partida.id)
		return HttpResponseRedirect(url_to_go)


# play da partida
class PartidaView(View):

	def get(self, request, id_partida):

		values = {}

		if request.user.is_authenticated:

			partida = Partida.objects.filter(id=id_partida, usuario_partida=request.user).first()
			
			# nao tem partida, vai pra 
			if partida == None:
				return HttpResponseRedirect("/nova_partida")


			if not partida.aberta :
				return HttpResponseRedirect("/nova_partida")


			# partida existe, vou setar todas as anteriores como abertas = False
			partidas_para_fechar = Partida.objects.filter(usuario_partida=request.user).exclude(id=id_partida)
			for partida_para_fechar in partidas_para_fechar:
				partida_para_fechar.aberta = False
				partida_para_fechar.save()


			
				
		else:
			return HttpResponseRedirect("/")
		
		
		values['partida'] = partida
		values['id_partida'] = id_partida

		values['categorias'] = (
			partida.q1_categoria_1.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q1_categoria_2.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q1_categoria_3.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q1_categoria_4.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q1_categoria_5.questao.pergunta.tipo_pergunta_ou_resposta,

			partida.q2_categoria_1.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q2_categoria_2.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q2_categoria_3.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q2_categoria_4.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q2_categoria_5.questao.pergunta.tipo_pergunta_ou_resposta,

			partida.q3_categoria_1.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q3_categoria_2.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q3_categoria_3.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q3_categoria_4.questao.pergunta.tipo_pergunta_ou_resposta,
			partida.q3_categoria_5.questao.pergunta.tipo_pergunta_ou_resposta,

			)

		return render(
		request,
		'stacksup/partida.html',
		context=values,
		)


# perguntas
class PartidaQuestaoView(View):

	def podeJogar(self, request, id_partida, id_questao):
		if request.user.is_authenticated:

			partida = Partida.objects.filter(id=id_partida, usuario_partida=request.user).first()

			if not partida.aberta:
				return (False, 0)

			respondeu = 0
			# pegando a questao
			# comeca no 1
			# vai ate 15
			qual_questao = partida.q1_categoria_1

			if partida.q1_categoria_1.resposta != None:
				if respondeu == 0:
					respondeu = 1
					qual_questao = partida.q1_categoria_2
			if partida.q1_categoria_2.resposta != None:
				if respondeu == 1:
					respondeu = 2
					qual_questao = partida.q1_categoria_3

			if partida.q1_categoria_3.resposta != None:
				if respondeu == 2:
					respondeu = 3
					qual_questao = partida.q1_categoria_4

			if partida.q1_categoria_4.resposta != None:
				if respondeu == 3:
					respondeu = 4
					qual_questao = partida.q1_categoria_5

			if partida.q1_categoria_5.resposta != None:
				if respondeu == 4:
					respondeu = 5
					qual_questao = partida.q2_categoria_1

			if partida.q2_categoria_1.resposta != None:
				if respondeu == 5:
					respondeu = 6
					qual_questao = partida.q2_categoria_2

			if partida.q2_categoria_2.resposta != None:
				if respondeu == 6:
					respondeu = 7
					qual_questao = partida.q2_categoria_3

			if partida.q2_categoria_3.resposta != None:
				if respondeu == 7:
					respondeu = 8
					qual_questao = partida.q2_categoria_4

			if partida.q2_categoria_4.resposta != None:
				if respondeu == 8:
					respondeu = 9
					qual_questao = partida.q2_categoria_5

			if partida.q2_categoria_5.resposta != None:
				if respondeu == 9:
					respondeu = 10
					qual_questao = partida.q3_categoria_1

			if partida.q3_categoria_1.resposta != None:
				if respondeu == 10:
					respondeu = 11
					qual_questao = partida.q3_categoria_2

			if partida.q3_categoria_2.resposta != None:
				if respondeu == 11:
					respondeu = 12
					qual_questao = partida.q3_categoria_3

			if partida.q3_categoria_3.resposta != None:
				if respondeu == 12:
					respondeu = 13
					qual_questao = partida.q3_categoria_4

			if partida.q3_categoria_4.resposta != None:
				if respondeu == 13:
					respondeu = 14
					qual_questao = partida.q3_categoria_5

			if partida.q3_categoria_5.resposta != None:
				if respondeu == 14:
					respondeu = 15
					qual_questao = None



			# print("AAA------------")

			# print(int(id_questao) == (respondeu + 1))
			# print(int(id_questao))
			# print((respondeu + 1))


			# se eu posso responder essa pergunta
			if int(id_questao) == (respondeu + 1) and qual_questao != None:
				return (True, (respondeu + 1), qual_questao)
			else:
				return (False, (respondeu+1))

				
		else:
			return (False, 0)

	def get(self, request, id_partida, id_questao):

		values = {}


		if request.user.is_authenticated:

			partida = Partida.objects.filter(id=id_partida, usuario_partida=request.user).first()

			# nao tem partida, vai pra 
			if partida == None:
				return HttpResponseRedirect("/nova_partida")


			# pegando a questao
			# comeca no 1
			# vai ate 15
			retornao = self.podeJogar(request, id_partida, id_questao)

			# se pode jogar
			if retornao[0]:
				values['questao'] = retornao[2]

				respostas = list(retornao[2].questao.respostas.all())

				# mudar ordem aqui
				shuffle(respostas)

				values['respostas'] = respostas

				values['partida_id'] = id_partida
				values['qst_id'] = id_questao
				if PrototipoQuestao.objects.filter(questao=retornao[2].questao).exists():
					values['is_prototipo'] = "partida"
				

			# se nao pode
			elif retornao[1] == 0:
				

				return HttpResponseRedirect("/" )
			else:

				return HttpResponseRedirect("/partida_questao/"+ id_partida +"/q/"+ str(retornao[1]) )
				
				
		else:
			return HttpResponseRedirect("/")
		
		# print("ASDSADSAD")
		# print(values)
		return render(
		request,
		'stacksup/partida_questao.html',
		context=values,
		)

	def post(self, request, id_partida, id_questao):
		
		# values = {}

		if request.user.is_authenticated:

			partida = Partida.objects.filter(id=id_partida, usuario_partida=request.user).first()

			reposta_dada_pelo_user = request.POST.get('botao_resposta', False)


			# pegando a questao
			# comeca no 1
			# vai ate 15
			retornao = self.podeJogar(request, id_partida, id_questao)

			# posso jogar essa questao
			if retornao[0]:
				# values['questao'] = retornao[2]
				respostas = retornao[2].questao.respostas.all()


				# sdasdas
				resp_certa = None
				resp_user= None
				# sdasdas

				# loop pelas possiveis respostas
				for resposta in respostas:


					# sdasdas
					todas_referencias = resposta.referencias.all()
					for refefe in todas_referencias:
						if refefe.pergunta == retornao[2].questao.pergunta:
							resp_certa = resposta
							break

					# sdasdas


					
					# qual resposta do usuario?
					narra = NarrativaString.objects.filter(resposta=resposta)
					for idioma in narra:
						# é a escolha do user
						if idioma.narrativa == reposta_dada_pelo_user:
						
							# sdasdas

							resp_user = resposta
							break

				# ja achei a certa e a do user

				# salvando
				retornao[2].resposta = resp_user
				retornao[2].data_resposta = timezone.now()
				retornao[2].save()

				# user ganhou
				if resp_user == resp_certa:
					

					# respondeu a 15 e acertou
					if retornao[1] == 15:
						
							
						partida.aberta = False
						partida.save()

						# dar pontos e moedas para o user
						# acertou tudo, multiplica por 3
						cart = Carteira.objects.select_related('user', 'carteira_de_premiacao').filter(user=request.user).first()
						quanto_moeda = partida.carteira_de_premiacao.moedas
						quanto_moeda = quanto_moeda * 3

						quanto_ponto = partida.carteira_de_premiacao.pontos * 3

						cart.moedas = cart.moedas + quanto_moeda
						cart.pontos = cart.pontos + quanto_ponto

						cart.save()

						return HttpResponseRedirect("/")


					# se ainda tem perguntas
					if retornao[1]+1 <= 15:
					
						# return HttpResponseRedirect("/partida_questao/"+ id_partida +"/q/"+ str(retornao[1]+1) )
						values = {}
						values['pos_jogo'] = retornao[2]
						values['respostas'] = retornao[2].questao.respostas.all()

						values['resposta_user'] = resp_user
						values['resposta_certa'] = resp_certa

						values['partida_id'] = id_partida
						values['questao_id'] = id_questao


						if PrototipoQuestao.objects.filter(questao=retornao[2].questao).exists():
							values['is_prototipo'] = "partida"

						return render(
							request,
							'stacksup/partida_questao.html',
							context=values,
						)

				# errou
				else:
					# resposta errada
					# resposta nem tem referencias

					partida.aberta = False
					partida.save()

					# dar ponsto para o user
					cart = Carteira.objects.filter(user=request.user).first()
					quanto_moeda = partida.carteira_de_premiacao.moedas
					quanto_moeda = quanto_moeda * int(retornao[1] / 5)

					quanto_ponto = partida.carteira_de_premiacao.pontos * int(retornao[1] / 5)

					cart.moedas = cart.moedas + quanto_moeda
					cart.pontos = cart.pontos + quanto_ponto
					cart.save()

					# return HttpResponseRedirect("/")
					values = {}
					values['pos_jogo'] = retornao[2]
					values['respostas'] = retornao[2].questao.respostas.all()

					values['resposta_user'] = resp_user
					values['resposta_certa'] = resp_certa

					values['partida_id'] = id_partida
					values['questao_id'] = id_questao

					if PrototipoQuestao.objects.filter(questao=retornao[2].questao).exists():
						values['is_prototipo'] = "partida"

					return render(
						request,
						'stacksup/partida_questao.html',
						context=values,
					)


							# sdasdas
							
							# # salvando
							# retornao[2].resposta = resposta
							# retornao[2].data_resposta = timezone.now()
							# retornao[2].save()


							# # verificando se resposta possui alguma referencia
							# # ou seja, se é verdadeira
							# referencias = resposta.referencias.all()
							# print("referencias-------------")
							# print(referencias)
							# if referencias:
								
							# 	# verificando se referencia é com a pergunta
							# 	for refe in referencias:
							# 		if refe.pergunta == retornao[2].questao.pergunta:
										
							# 			# opa, resposta correta


							# 			# respondeu a 15 e acertou
							# 			if retornao[1] == 15:
										
											
							# 				partida.aberta = False
							# 				partida.save()

							# 				# dar pontos e moedas para o user
							# 				# acertou tudo, multiplica por 3
							# 				cart = Carteira.objects.filter(user=request.user).first()
							# 				quanto_moeda = partida.carteira_de_premiacao.moedas
							# 				quanto_moeda = quanto_moeda * 3

							# 				cart.moedas = cart.moedas + quanto_moeda
							# 				cart.save()

							# 				return HttpResponseRedirect("/")


							# 			# se ainda tem perguntas
							# 			if retornao[1]+1 <= 15:
										
							# 				# return HttpResponseRedirect("/partida_questao/"+ id_partida +"/q/"+ str(retornao[1]+1) )
							# 				values = {}
							# 				values['pos_jogo'] = retornao[2]

							# 				values['respostas'] = retornao[2].questao.respostas.all()
							# 				if PrototipoQuestao.objects.filter(questao=retornao[2].questao).exists():
							# 					values['is_prototipo'] = "partida"
							# 				return render(
							# 					request,
							# 					'stacksup/partida_questao.html',
							# 					context=values,
							# 				)

							# 	# resposta errada
							# 	# resposta possui referencia mas não para a pergunta atual
							# 	partida.aberta = False
							# 	partida.save()

							# 	# dar ponsto para o user
							# 	cart = Carteira.objects.filter(user=request.user).first()
							# 	quanto_moeda = partida.carteira_de_premiacao.moedas
							# 	quanto_moeda = quanto_moeda * (retornao[1] % 5)

							# 	cart.moedas = cart.moedas + quanto_moeda
							# 	cart.save()

								
							# 	# return HttpResponseRedirect("/")
							# 	values = {}
							# 	values['pos_jogo'] = 1
							# 	return render(
							# 		request,
							# 		'stacksup/partida_questao.html',
							# 		context=values,
							# 	)
							# else:
							# 	# resposta errada
							# 	# resposta nem tem referencias

							# 	partida.aberta = False
							# 	partida.save()

							# 	# dar ponsto para o user
							# 	cart = Carteira.objects.filter(user=request.user).first()
							# 	quanto_moeda = partida.carteira_de_premiacao.moedas
							# 	quanto_moeda = quanto_moeda * (retornao[1] % 5)

							# 	cart.moedas = cart.moedas + quanto_moeda
							# 	cart.save()

							# 	# return HttpResponseRedirect("/")
							# 	values = {}
							# 	values['pos_jogo'] = 1
							# 	return render(
							# 		request,
							# 		'stacksup/partida_questao.html',
							# 		context=values,
							# 	)

							# # # se ainda tem perguntas
							# # if retornao[1]+1 <= 15:
							
							# # 	return HttpResponseRedirect("/partida_questao/"+ id_partida +"/q/"+ str(retornao[1]+1) )
							# # # se ja acabou
							# # else:
							# # 	partida.aberta = False
							# # 	partida.save()
							# # 	return HttpResponseRedirect("/")

			# não pode jogar essa questao, mas pode alguma
			elif retornao[1] > 0 and retornao[1] <= 15:
				return HttpResponseRedirect("/partida_questao/"+ id_partida +"/q/"+ str(retornao[1]) )

			# nao tem partida, vai pra 
			if partida == None:
				return HttpResponseRedirect("/nova_partida")
				
		else:
			return HttpResponseRedirect("/")


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

			# logs das partidas
			logs = []
			partidas = Partida.objects.select_related('usuario_partida').filter(usuario_partida=request.user).order_by('-id')

			try:
				for partida in partidas:
					# part_log = (partida)
					logs.append( partida )

			except Exception as e:
				raise

			user = user.first()

		else:
			# user = None
			# carteira = None
			return HttpResponseRedirect("/login")

		values['usuario'] = user
		values['carteira'] = carteira
		values['questoes'] = qs

		values['regioes'] = regioes

		# fazer depois
		values['logs'] = logs



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

		# criando questoes
		# receber o tipo do usuario
		if textoPerguntaQuestao != False and textoRespostaCorreta != False:

			regiao_da_questao = request.POST.get('regiaoFormControlSelectQuestao', False)

			regiao_pergunta = Regiao.objects.filter(nome=regiao_da_questao).first()

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


				# pos a questao ainda esta em avaliação
				proto_questao = PrototipoQuestao(questao=questao)
				proto_questao.save()




			except Exception as e:
				raise


		# criando regioes
		# elif nomeDaRegiao != False:

		# 	regiao_pai_nome = request.POST.get('regiaoFormControlSelect', False)
			
		# 	try:
		# 		regiao = Regiao(nome=nomeDaRegiao)

		# 		regiao_pai = Regiao.objects.filter(nome=regiao_pai_nome).first()

		# 		regiao.save()
		# 		criado_por = "Criado por: " + str(request.user)
		# 		conexao = ConexaoRegiao(nome=criado_por, reg1=regiao_pai ,reg2=regiao)

		# 		conexao.save()
			
		# 	except Exception as e:
		# 		raise

		else:
			return HttpResponseRedirect("/fabrica")


		
		return HttpResponseRedirect("/fabrica")
		



		
		
