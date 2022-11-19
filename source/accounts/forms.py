from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Login')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm the password", required=True, widget=forms.PasswordInput, strip=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        first_name = cleaned_data.get('first_name')
        email = cleaned_data.get('email')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        elif not email:
            raise forms.ValidationError('Field "Email address" is required!')
        elif not first_name:
            raise forms.ValidationError('Field "First name" is required!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        # user.groups.add('user')
        if commit:
            user.save()
        return user

