from django import forms
from .models import Users
from django.forms import ModelForm

class SignUpForm(ModelForm):
    class Meta():
        model=Users
        fields='__all__'
        widgets={
                "name":forms.TextInput(attrs={'class':'form-control ','placeholder':'Full Name'}),
                "email":forms.EmailInput(attrs={'class':'form-control ','placeholder':'example@gmail.com'}),
                "username":forms.TextInput(attrs={'class':'form-control ','placeholder':'xyz493'}),
                "password":forms.PasswordInput(attrs={'class':'form-control '})
                }

