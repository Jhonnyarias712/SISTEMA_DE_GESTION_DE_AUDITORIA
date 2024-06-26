# Generated by Django 5.0.6 on 2024-05-20 02:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0006_rename_auditar_auditoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionActividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.CharField(choices=[('APROBADA', 'Aprobada'), ('REPROBADA', 'Reprobada')], max_length=10)),
                ('observaciones', models.CharField(max_length=1000)),
                ('plazo_ini_observacion', models.DateTimeField()),
                ('plazo_fin_observacion', models.DateTimeField()),
                ('auditoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LOGIN.auditoria')),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LOGIN.formulario')),
            ],
        ),
    ]
