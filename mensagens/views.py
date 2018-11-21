from django.shortcuts import render

from django.views.generic import View

from usuario_perfil.models import UserProfile

# Create your views here.


class Index(View):

	def get(self, request):

		values = {}

		if request.user.is_authenticated:
			user = UserProfile.objects.filter(nome=request.user) 
		else:
			user = None

		values['usuario'] = user

		return render(
		request,
		'contatos.html',
		context=values,
		)




