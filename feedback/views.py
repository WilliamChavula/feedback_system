from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from better_profanity import profanity

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
        profanity.load_censor_words()
        feedback = form.save(commit=False)
        feedback.student = self.request.user

        if profanity.contains_profanity(feedback.feedback_text):
            messages.error(
                self.request,
                "The text may contain words flagged as being profane. Feedback not saved!",
            )

            return super(AddFeedbackView, self).form_invalid(form)

        feedback.save()
        return super(AddFeedbackView, self).form_valid(form)
