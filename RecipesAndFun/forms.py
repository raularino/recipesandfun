from django import forms
from .models import receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model=receta
        fields = ('nombre_receta','ingredientes','preparacion','tiempo_preparacion')