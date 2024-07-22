# forms.py
from django import forms
from .models import AgendaAuditorias, Auditoria, EvaluacionActividad, Formulario

class AgendaAuditoriasForm(forms.ModelForm):
    class Meta:
        model = AgendaAuditorias
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
            'fecha_fin': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
        help_texts = {
            'fecha_inicio': 'Formato esperado: YYYY-MM-DD HH:MM',
            'fecha_fin': 'Formato esperado: YYYY-MM-DD HH:MM',
        }

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = '__all__'
        widgets = {
            'fecha_inicio_auditoria': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
            'fecha_fin_auditoria': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
            'fecha_inicio_plazo': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
            'fecha_fin_plazo': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
            'fecha_cierre_auditoria': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
        help_texts = {
            'fecha_inicio_auditoria': 'Formato esperado: YYYY-MM-DD HH:MM',
            'fecha_fin_auditoria': 'Formato esperado: YYYY-MM-DD HH:MM',
            'fecha_inicio_plazo': 'Formato esperado: YYYY-MM-DD HH:MM',
            'fecha_fin_plazo': 'Formato esperado: YYYY-MM-DD HH:MM',
            'fecha_cierre_auditoria': 'Formato esperado: YYYY-MM-DD HH:MM',
        }
        
class AuditarForm(forms.ModelForm):
    class Meta:
        model = EvaluacionActividad
        fields = '__all__'
        widgets = {
            'plazo_ini_observacion': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
            'plazo_fin_observacion': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
        help_texts = {
            'plazo_ini_observacion': 'Formato esperado: YYYY-MM-DD HH:MM',
            'plazo_fin_observacion': 'Formato esperado: YYYY-MM-DD HH:MM',
        }
        
class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'