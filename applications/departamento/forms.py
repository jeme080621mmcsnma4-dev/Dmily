from django import forms

class NewDepartamentoForms(forms.Form):
    nombre = forms.CharField(max_length=50, label="Departamento")
    short_name = forms.CharField(max_length=20, label="Short name")
