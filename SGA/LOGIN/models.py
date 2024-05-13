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
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    actividad = models.CharField(max_length=1200)

    def __str__(self):
        return f"Formulario {self.id} - {self.actividad}"