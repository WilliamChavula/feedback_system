from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegistrationForm


class UserRegistrationView(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy("account:login")
    template_name = "account/signup.html"
