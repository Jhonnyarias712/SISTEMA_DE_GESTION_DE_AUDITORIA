from django.contrib import admin
from .models import USERS,Plantilla,Formulario,AgendaAuditorias,Auditoria,EvaluacionActividad,HistorialAuditoria

admin.site.register(USERS)
admin.site.register(Plantilla)
admin.site.register(Formulario)
admin.site.register(AgendaAuditorias)
admin.site.register(Auditoria)
admin.site.register(EvaluacionActividad)
admin.site.register(HistorialAuditoria)

# Register your models here.
