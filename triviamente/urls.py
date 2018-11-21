from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('narrativa', views.NarrativaView)

urlpatterns = [

	path('api/', include(router.urls)),

	path('', views.Index.as_view())




]
