from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm,forms


class CsvFiles(forms.Form):
    csv = forms.FileField(allow_empty_file=False)


class Profile_F(UserCreationForm):


   """ email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)"""
   class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email')
