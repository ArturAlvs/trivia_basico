from django.shortcuts import render

from django.views.generic import View
from rest_framework import viewsets, permissions
from .models import Referencia, Pergunta, Resposta, NarrativaString, Questao, PrototipoQuestao, OpiniaoQuestao, OpiniaoPergunta, OpiniaoResposta
from .serializers import ReferenciaSerializer, PerguntaSerializer, RespostaSerializer, NarrativaStringSerializer, QuestaoSerializer, PrototipoQuestaoSerializer, OpiniaoQuestaoSerializer, OpiniaoPerguntaSerializer, OpiniaoRespostaSerializer

from .permissions import IsAllowedToWriteIfOwnAndReadIfLogged

from usuario_perfil.models import UserProfile
from value.models import Carteira

class NarrativaView(viewsets.ModelViewSet):

	queryset = NarrativaString.objects.all()

	serializer_class = NarrativaStringSerializer

	permission_classes = (IsAllowedToWriteIfOwnAndReadIfLogged,)



class Index(View):

	def get(self, request):

		values = {}

		if request.user.is_authenticated:
			user = UserProfile.objects.filter(nome=request.user) 

			carteira = Carteira.objects.filter(user=request.user).first()



			user = user.first()

		else:
			user = None
			carteira = None

		values['usuario'] = user
		values['carteira'] = carteira

		return render(
		request,
		'index.html',
		context=values,
		)





