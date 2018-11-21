from django.contrib import admin

from .models import Carta, Album, Carteira, Compra


# Register your models here.


admin.site.register(Carta)
admin.site.register(Album)
admin.site.register(Carteira)
admin.site.register(Compra)
