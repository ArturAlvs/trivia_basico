from django.shortcuts import render

from django.http import HttpResponseRedirect


from django.views.generic import View

from usuario_perfil.models import UserProfile

from .models import MSG_PARA_SYST

# Create your views here.


class Index(View):

	def get(self, request):

		values = {}

		if request.user.is_authenticated:
			user = UserProfile.objects.filter(nome=request.user) 
			
			values['usuario'] = user
		else:
			user = None


		return render(
		request,
		'contatos.html',
		context=values,
		)



	def post(self, request):

		if request.user.is_authenticated:
			user = UserProfile.objects.filter(nome=request.user) 
		else:
			return HttpResponseRedirect("/contato")
			

		motivo = request.POST.get('motivo', False)
		texto_enviado_pelo_user = request.POST.get('texto_enviado_pelo_user', False)

		# print("email----------")
		# print(email)
		# print(motivo)
		# print(texto_enviado_pelo_user)

		if texto_enviado_pelo_user == False or texto_enviado_pelo_user == "" or motivo == False:
			return HttpResponseRedirect("/contato")
		else:

		# 	("S", "Sugestão"),
		# ("R", "Reclamação"),
		# ("O", "Outros"),

			if motivo == "Sugestão":
				motivo = "S"
			elif motivo == "Reclamação":
				motivo = "R"
			elif motivo == "Outros":
				motivo = "O"
			
			msg = MSG_PARA_SYST(tipo_mensagem=motivo, user=request.user, texto=texto_enviado_pelo_user)
			msg.save()

		return HttpResponseRedirect("/contato")

		
		





