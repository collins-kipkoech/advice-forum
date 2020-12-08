from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


ROLE_CHOICES = [
	(1, '1 - Regular User'),
	(2, '2 - counsellor'),
	(3, '3 - Mentor'),
	
]
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username','role','email','password1','password2']