from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
	path('', views.Index.as_view()),
	path('nova_partida/', views.NovaPartida.as_view()),

	path('fabrica/', views.FabricaView.as_view()),

	# path('partida/', views.Partida.as_view()),

	url(r'^partida/(?P<id_partida>\d+)/', views.PartidaView.as_view()),
	url(r'^partida_questao/(?P<id_partida>\d+)/q/(?P<id_questao>\d+)', views.PartidaQuestaoView.as_view()),

]
