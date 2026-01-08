from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo', 
            'subtitulo', 
            'cantidad'
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingresa texto aquí'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingresa texto aquí'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingresa un número aquí'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is not None and cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        return cantidad
