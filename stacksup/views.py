from django.shortcuts import render

from django.views.generic import View
from usuario_perfil.models import UserProfile
from value.models import Carteira

from triviamente.models import Questao, NarrativaString, Pergunta, Resposta, Referencia, PrototipoQuestao


from regionamento.models import Regiao, Idioma, ConexaoRegiao

from django.http import HttpResponseRedirect

from .models import Partida, SUQuestionLog

from random import randint

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

				# pego as perguntas
				pergunta = Pergunta.objects.filter(tipo_pergunta_ou_resposta=categoria_questao).all()
				# escolho uma

				print("pergunta----------")
				print(categorias_existentes)
				print(categoria_questao)
				print(pergunta)
				print("pergunta----------")

				qual_pergunta = randint(0, (len(pergunta)-1))
				# seleciono a escolhida
				pergunta = pergunta[qual_pergunta]

				questao = Questao.objects.filter(pergunta=pergunta).first()

				questoes_escolhidas_p_partida.append(questao)


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


class PartidaView(View):

	def get(self, request, id_partida):

		values = {}

		if request.user.is_authenticated:

			partida = Partida.objects.filter(id=id_partida, usuario_partida=request.user).first()

			# nao tem partida, vai pra 
			if partida == None:
				return HttpResponseRedirect("/nova_partida")
				
		else:
			return HttpResponseRedirect("/")
		
		
		values['partida'] = partida

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
		



		
		
