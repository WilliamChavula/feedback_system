from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import LoginForm
from .views import UserRegistrationView

app_name = "account"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="account/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="account/logout.html"),
        name="logout",
    ),
    path("register/", UserRegistrationView.as_view(), name="register"),
]
