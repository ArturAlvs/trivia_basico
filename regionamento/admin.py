from django.contrib import admin


from .models import Idioma, Regiao, ConexaoRegiao, OpiniaoRegiao, OpiniaoConexao


admin.site.register(Idioma)
admin.site.register(Regiao)
admin.site.register(ConexaoRegiao)
admin.site.register(OpiniaoRegiao)
admin.site.register(OpiniaoConexao)
