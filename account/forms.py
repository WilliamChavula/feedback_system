from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

AppUser = get_user_model()


class LoginForm(AuthenticationForm):
    class Meta:
        exclude = ("email",)

    username = forms.CharField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700"
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700"
            }
        ),
    )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ("username", "password1", "password2")

    username = forms.CharField(
        label="Email",
        widget=forms.TextInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3 "
                         "focus:outline-none focus:border-blue-700"
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
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
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3 "
                         "focus:outline-none focus:border-blue-700"
            }
        ),
    )

    def clean_password2(self) -> str:
        form_dict = self.cleaned_data

        if form_dict["password"] != form_dict["password2"]:
            raise forms.ValidationError("Passwords do not match")
        return form_dict["password2"]
