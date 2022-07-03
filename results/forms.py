from django import forms
from .models import *


class Sem1IaForm(forms.ModelForm):
    class Meta:
        model = IaSem1
        fields = '__all__'

class Sem2IaForm(forms.ModelForm):
    class Meta:
        model = IaSem2
        fields = '__all__'

class Sem3IaForm(forms.ModelForm):
    class Meta:
        model = IaSem3
        fields = '__all__'

class Sem4IaForm(forms.ModelForm):
    class Meta:
        model = IaSem4
        fields = '__all__'
