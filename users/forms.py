from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    FirstName = forms.CharField(max_length=30)
    LastName = forms.CharField(max_length=30)

    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model=User
        fields=['username', 'FirstName', 'LastName', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
        exclude = ['FirstName', 'LastName']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['image']

