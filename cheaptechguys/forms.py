from django import forms
from .models import contact_us
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'



