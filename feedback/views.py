from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from account.models import AppUser
from .forms import AddFeedbackForm
from .models import Feedback


class FeedbackListView(ListView):
    model = Feedback
    context_object_name = "list"
    template_name = "feedback/list.html"


class AddFeedbackView(LoginRequiredMixin, CreateView):
    form_class = AddFeedbackForm
    success_url = reverse_lazy("feedback:list")
    template_name = "feedback/add.html"

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.student = self.request.user

        feedback.save()

        return super(AddFeedbackView, self).form_valid(form)
