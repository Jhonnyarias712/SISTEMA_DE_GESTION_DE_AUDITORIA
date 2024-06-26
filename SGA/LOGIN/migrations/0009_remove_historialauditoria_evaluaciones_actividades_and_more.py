# Generated by Django 5.0.6 on 2024-05-20 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0008_historialauditoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historialauditoria',
            name='evaluaciones_actividades',
        ),
        migrations.AddField(
            model_name='historialauditoria',
            name='evaluaciones_actividades',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='LOGIN.evaluacionactividad'),
            preserve_default=False,
        ),
    ]