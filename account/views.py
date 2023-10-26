from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


class UserRegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("account:login")
    template_name = "account/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("feedback:add")

        return super(UserRegistrationView, self).dispatch(request, *args, **kwargs)
