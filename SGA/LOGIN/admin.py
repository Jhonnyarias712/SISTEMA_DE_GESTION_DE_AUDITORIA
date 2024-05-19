from django.contrib import admin
from .models import USERS,Plantilla,Formulario,AgendaAuditorias

admin.site.register(USERS)
admin.site.register(Plantilla)
admin.site.register(Formulario)
admin.site.register(AgendaAuditorias)

# Register your models here.
