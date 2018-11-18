from rest_framework import serializers

from .models import Pergunta, Resposta, NarrativaString, Questao, PrototipoQuestao, OpiniaoQuestao, OpiniaoPergunta, OpiniaoResposta, Referencia


class PerguntaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Pergunta

		fields = ('tipo_pergunta_ou_resposta')


class RespostaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Resposta

		fields = ('referencias')

class ReferenciaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Referencia

		fields = ('pergunta', 'texto')


class NarrativaStringSerializer(serializers.ModelSerializer):

	class Meta:
		model = NarrativaString

		fields = ('url', 'tipo_pergunta_ou_resposta', 'pergunta', 'resposta', 'user_criador', 'idioma', 'narrativa')

class QuestaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Questao

		fields = ('dificuldade', 'user_criador', 'pergunta', 'resposta_1', 'resposta_2', 'resposta_3', 'resposta_4', 'regiao', 'data_criacao')

class PrototipoQuestaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = PrototipoQuestao

		fields = ('questao', 'user_criador', 'reclamacao', 'data_criacao')

class OpiniaoQuestaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = OpiniaoQuestao

		fields = ('questao', 'reclamacao', 'data_criacao_opiniao')

class OpiniaoPerguntaSerializer(serializers.ModelSerializer):

	class Meta:
		model = OpiniaoPergunta

		fields = ('pergunta', 'user_criador', 'reclamacao', 'data_criacao_opiniao')

class OpiniaoRespostaSerializer(serializers.ModelSerializer):

	class Meta:
		model = OpiniaoResposta

		fields = ('resposta', 'user_criador', 'reclamacao', 'data_criacao_opiniao')




