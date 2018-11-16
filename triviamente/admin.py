from django.contrib import admin

from .models import Pergunta, Resposta, NarrativaString, Questao, PrototipoQuestao, OpiniaoQuestao, OpiniaoPergunta, OpiniaoResposta

# Register your models here.


admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(NarrativaString)
admin.site.register(Questao)
admin.site.register(PrototipoQuestao)
admin.site.register(OpiniaoQuestao)
admin.site.register(OpiniaoPergunta)
admin.site.register(OpiniaoResposta)
