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

    course_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of Course",
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3 "
                         "focus:outline-none focus:border-blue-700",
            }
        ),
    )

    course_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Code",
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-1 "
                         "focus:outline-none focus:border-blue-700",
            }
        ),
    )

    professor = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Professor",
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-1 "
                         "focus:outline-none focus:border-blue-700",
            }
        ),
        help_text="Who teaches this course?",
    )

    feedback_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write your review",
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-1 "
                         "focus:outline-none focus:border-blue-700",
            }
        ),
        help_text="Obscene language is not accepted. Please be kind, polite, and constructive in your review.",
    )
