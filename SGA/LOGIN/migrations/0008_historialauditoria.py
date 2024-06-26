# Generated by Django 5.0.6 on 2024-05-20 02:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0007_evaluacionactividad'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialAuditoria',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio_auditoria', models.DateTimeField()),
                ('fecha_fin_auditoria', models.DateTimeField()),
                ('estado_auditoria', models.CharField(choices=[('APROBADA', 'Aprobada'), ('REPROBADA', 'Reprobada'), ('PENDIENTE', 'Pendiente'), ('CANCELADA', 'Cancelada')], max_length=10)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('documentos_adjuntos', models.FileField(blank=True, null=True, upload_to='documentos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('auditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LOGIN.users')),
                ('auditoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LOGIN.auditoria')),
                ('evaluaciones_actividades', models.ManyToManyField(blank=True, related_name='historiales_auditoria', to='LOGIN.evaluacionactividad')),
                ('fk_plantilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LOGIN.plantilla')),
            ],
        ),
    ]
