from django import forms
from django.core.exceptions import ValidationError


class UserRegister(forms.Form):
    username = forms.CharField(max_length=100, label='Введите логин:')
    password = forms.CharField(widget=forms.PasswordInput, min_length=8,
                               label='Введите пароль:')
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8,
                                      label='Повторите пароль:')
    age = forms.IntegerField(min_value=1, max_value=100, label='Введите свой возраст:')