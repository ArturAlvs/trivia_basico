from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from regionamento.models import Regiao, Idioma
from value.models import Carteira, Album


class Login(View):

	def get(self, request):

		if request.user.is_authenticated:
			return HttpResponseRedirect("/")


		return render(
		request,
		'login.html',
		context={},
		)

	def post(self, request):
		usuario = request.POST['usuario']
		password = request.POST['password']

		if usuario == "":
			return render(request, 'login.html', {'error': "Usuario é obrigatório"})

		if password == "":
			return render(request, 'login.html', {'error': "Senha é obrigatório"})

		user = authenticate(request, username=usuario, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			return render(request, 'login.html', {'error': "Usuário não encontrado"})


class Logout(View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect("/")


class UpdateCadastro(View):

	def get(self, request):

		if not request.user.is_authenticated:
			return HttpResponseRedirect("/login")

		regioes = Regiao.objects.all()
		idiomas = Idioma.objects.all()

		user = UserProfile.objects.filter(user=request.user).first()



		return render(
			request,
			'meu_cadastro.html',
			context={
			'regioes': regioes, 'idiomas': idiomas, 
			'user_perfil': user, 'user': request.user,
			'regioes_usuario': user.regioes.all(),
			'idiomas_usuario': user.idiomas.all(),
			},
		)


	# melhorar bastante essa parte
	def post(self, request):
		
		user = request.user


		name = request.POST.get('name', False)
		email = request.POST.get('email', False)
		novoPassword = request.POST.get('novoPassword', False)
		gender = request.POST.get('gender', False)
		age = request.POST.get('age', False)
		regiao = request.POST.get('regiao', False)
		idioma = request.POST.get('idioma', False)


		if len(novoPassword) > 3:
			user.set_password(novoPassword)

		user.email = email
		user.save()


		profile = user.user

		profile.name = name
		profile.age = age
		profile.gender = gender


		regiaoObj = Regiao.objects.filter(nome=regiao).first()

		idiomaObj = Idioma.objects.filter(nome=idioma).first()

		if not regiaoObj in profile.regioes.all() and regiaoObj != None:
			profile.regioes.add(regiaoObj)

		if not idiomaObj in profile.idiomas.all() and idiomaObj != None:

			profile.idiomas.add(idiomaObj)


		profile.save()



		# return render(
		# 	request,
		# 	'meu_cadastro.html',
		# )

		return HttpResponseRedirect("/cadastro")






class Register(View):

	def get(self, request):

		regioes = Regiao.objects.all()
		idiomas = Idioma.objects.all()

		return render(
			request,
			'register.html',
			context={'regioes': regioes, 'idiomas': idiomas},
		)

	def post(self, request):

		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			userObj = form.cleaned_data
			email = userObj['email']
			password = userObj['password']

			confirm_password = userObj['confirmPassword']
			gender = request.POST['gender']
			username = request.POST['name']
			age = request.POST['age']

			# vem uma regiao só
			regiao = request.POST['regiao']

			idioma = request.POST['idioma']


			regiaoObj = Regiao.objects.filter(nome=regiao).first()

			idiomaObj = Idioma.objects.filter(nome=idioma).first()

			if username == '':
				username = email.split('@')[0]


			
			if password != confirm_password:
				error = "As senha são diferentes"
				return render(request, 'register.html', {"error": error})
			elif User.objects.filter(username=username).exists() and not User.is_authenticated:
				error = "Usuario já cadastrado"
				return render(request, 'register.html', {"error": error})
			else:
				try:
					# tirar tudo depois do @ do email para ser o usuario
					user = User.objects.create_user(username=username, email=email, password=password)
					user.save()

					# profile
					profile = UserProfile(user=user)
					profile.nome = username
					profile.age = int(age)
					profile.gender = gender
					profile.save()
					profile.regioes.add(regiaoObj)
					profile.idiomas.add(idiomaObj)

					# carteira
					carteira = Carteira(user=user)
					carteira.save()

					album = Album(user=user)
					album.save()


					login(request, user)
				except:
					return render(request, 'register.html', {'error': 'Erro ao salvar usuário, possível email já cadastrado.'})

				# return render(request, 'index.html', {'register_success': True})
				return HttpResponseRedirect("/")

		else:
			required_fileds = []
			for k in list(form.errors.keys()):
				required_fileds.append(k)
			return render(request, 'register.html', {'form_errors': required_fileds})

