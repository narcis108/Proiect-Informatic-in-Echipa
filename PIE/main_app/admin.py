from django.contrib import admin

# Register your models here.
from main_app.models import Utilizator, Film, Actor, Distributie, Regie, Gen, GenuriFilm, Regizor

admin.site.register(Utilizator)
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Distributie)
admin.site.register(Regie)
admin.site.register(Gen)
admin.site.register(GenuriFilm)
admin.site.register(Regizor)
