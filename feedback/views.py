from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddFeedbackForm
from .models import Feedback


class FeedbackListView(ListView):
    model = Feedback
    context_object_name = "list"
    template_name = "feedback/list.html"


class AddFeedbackView(LoginRequiredMixin, FormView):
    form_class = AddFeedbackForm
    success_url = reverse_lazy("feedback:list")
