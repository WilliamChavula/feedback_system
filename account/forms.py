from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import validate_email

from .models import AppUser


class LoginForm(AuthenticationForm):
    class Meta:
        exclude = ("email",)

    username = forms.CharField(
        validators=[validate_email],
        label="Email",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3"
                " focus:outline-none focus:border-blue-700"
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3"
                " focus:outline-none focus:border-blue-700"
            }
        ),
    )

    def clean_username(self) -> str:
        input_username: str = self.cleaned_data["username"]

        if input_username == "":
            raise forms.ValidationError("Username field cannot be empty")

        return input_username

    def clean_password(self) -> str:
        input_password: str = self.cleaned_data["password"]

        if input_password == "":
            raise forms.ValidationError("Password field cannot be empty")

        return input_password


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")

    email = forms.CharField(
        label="Email",
        required=False,
        validators=[validate_email],
        widget=forms.EmailInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3 "
                "focus:outline-none focus:border-blue-700"
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        required=False,
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3 "
                "focus:outline-none focus:border-blue-700"
            }
        ),
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3 "
                "focus:outline-none focus:border-blue-700"
            }
        ),
    )

    def clean_email(self) -> str:
        input_email: str = self.cleaned_data["email"]

        if input_email == "":
            raise forms.ValidationError("Email field cannot be empty")

        domain: str = input_email.split("@")[1]

        if "smu.edu" not in domain:  # Todo: improve
            raise forms.ValidationError("Must be a valid smu email address")

        return input_email

    def clean_password1(self) -> str:
        input_password: str = self.cleaned_data["password1"]

        if input_password == "":
            raise forms.ValidationError("Password field cannot be empty")

        return input_password

    def clean_password2(self) -> str:
        form_dict = self.cleaned_data

        if form_dict["password2"] == "":
            raise forms.ValidationError("Password Confirmation field cannot be blank")

        if form_dict["password1"] != form_dict["password2"]:
            raise forms.ValidationError("Passwords do not match")
        return form_dict["password2"]

    def save(self, commit=True):
        instance = super(RegistrationForm, self).save(commit=False)
        instance.username = self.cleaned_data["email"]

        if commit:
            instance.save()

        return instance
