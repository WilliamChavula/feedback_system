from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddFeedbackForm
from .models import Feedback
from .service import CensorService, ICensorService


class FeedbackListView(ListView):
    model = Feedback
    context_object_name = "list"
    template_name = "feedback/list.html"


class AddFeedbackView(LoginRequiredMixin, CreateView):
    form_class = AddFeedbackForm
    success_url = reverse_lazy("feedback:success")
    template_name = "feedback/add.html"
    service: ICensorService = CensorService()

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.student = self.request.user

        if self.service.has_profane(feedback.feedback_text):
            messages.error(
                self.request,
                "The text may contain words flagged as being profane. This feedback was not saved!",
            )

            return super(AddFeedbackView, self).form_invalid(form)

        feedback.save()
        return super(AddFeedbackView, self).form_valid(form)


class AddFeedbackSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "feedback/success.html"
