from django.db import models

class USERS(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=1)

    def __str__(self):
        return self.usuario
    
class Plantilla(models.Model):
    id_plantilla = models.AutoField(primary_key=True)
    nombre_plantilla = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    owner = models.ForeignKey(USERS, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.nombre_plantilla

class Formulario(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    actividad = models.CharField(max_length=1200)

    def __str__(self):
        return f"Formulario {self.id_actividad} - {self.actividad}"
    
class AgendaAuditorias(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    nombre_entidad = models.CharField(max_length=255)
    tipo_entidad = models.CharField(max_length=100)
    sector_industria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    contacto_entidad_email = models.EmailField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    duracion_dia = models.IntegerField()
    area_departamento = models.CharField(max_length=255)
    auditor = models.ForeignKey(USERS, on_delete=models.CASCADE)
    fk_plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    objetivo = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.nombre_entidad}/{self.auditor}: {self.objetivo}"

class Auditoria(models.Model):
    id_auditar = models.AutoField(primary_key=True)
    agenda_auditorias = models.ForeignKey(AgendaAuditorias, on_delete=models.CASCADE)
    fecha_inicio_auditoria = models.DateTimeField()
    fecha_fin_auditoria = models.DateTimeField()
    fecha_inicio_plazo = models.DateTimeField(blank=True, null=True)
    estado_auditoria = models.CharField(max_length=10, choices=[("EVALUANDO", "Evaluando")])
    observacion = models.TextField(blank=True, null=True)
    fecha_fin_plazo = models.DateTimeField(blank=True, null=True)
    fecha_cierre_auditoria = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Auditar ID: {self.id_auditar} - Estado: {self.estado_auditoria} - Fecha Inicio: {self.fecha_inicio_auditoria.strftime('%Y-%m-%d')} - Fecha Fin: {self.fecha_fin_auditoria.strftime('%Y-%m-%d')}"

class EvaluacionActividad(models.Model):
    id = models.AutoField(primary_key=True)
    auditoria_id = models.ForeignKey(Auditoria, on_delete=models.CASCADE)
    id_actividad = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=10, choices=[("APROBADA", "Aprobada"), ("REPROBADA", "Reprobada")])
    observaciones = models.CharField(max_length=1000)
    plazo_ini_observacion = models.DateTimeField()
    plazo_fin_observacion = models.DateTimeField()

    def __str__(self):
        return f"Evaluación: {self.id} - Estado Final: {self.respuesta} - Auditoría: {self.auditoria_id.id_auditar} - Observación: {self.observaciones}"
    
class HistorialAuditoria(models.Model):
    id_historial = models.AutoField(primary_key=True)
    auditoria = models.ForeignKey('Auditoria', on_delete=models.CASCADE)
    fecha_inicio_auditoria = models.DateTimeField()
    fecha_fin_auditoria = models.DateTimeField()
    estado_auditoria = models.CharField(max_length=10, choices=[("APROBADA", "Aprobada"), ("REPROBADA", "Reprobada"), ("PENDIENTE", "Pendiente"), ("CANCELADA", "Cancelada")])
    observaciones = models.TextField(blank=True, null=True)
    auditor = models.ForeignKey('USERS', on_delete=models.CASCADE)
    fk_plantilla = models.ForeignKey('Plantilla', on_delete=models.CASCADE)
    documentos_adjuntos = models.FileField(upload_to='documentos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    evaluaciones_actividades = models.ForeignKey('EvaluacionActividad', on_delete=models.CASCADE)

    def __str__(self):
        return f"Historial de Auditoría para {self.auditoria}"