from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя', 'class': 'form-control py-4'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль', 'class': 'form-control py-4'}))
    class Meta:
        model = User
        fields = ("username", "password")

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя', 'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию', 'class': 'form-control py-4'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя', 'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес эл. почты', 'class': 'form-control py-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль', 'class': 'form-control py-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль', 'class': 'form-control py-4'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')