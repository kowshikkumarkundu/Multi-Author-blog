from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "John",
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Doe",
            }),

            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "johndoe",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "john@example.com",
            }),
        }
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "w-full pl-10 pr-4 py-3 bg-surface-container-lowest border border-outline-variant rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-all outline-none",
            "placeholder":"••••••••"
        })
    )
    password2 = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': "w-full pl-10 pr-4 py-3 bg-surface-container-lowest border border-outline-variant rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-all outline-none",
                "placeholder":"••••••••"
            })
        )


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Enter username",
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Enter password",
        })
    )