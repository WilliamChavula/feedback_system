from django import forms

from .models import Feedback


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            "course_name",
            "course_code",
            "professor",
            "feedback_text",
        )
