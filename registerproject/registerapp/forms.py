from django import forms
from .models import Register

class Reg_Form(forms.ModelForm):
    class Meta:
        model=Register
        fields=['Fullname','Username','Password','email','image']