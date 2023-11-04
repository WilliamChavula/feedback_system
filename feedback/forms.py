from django import forms

from .models import Feedback


def validate_field_not_empty(value, field_name="Field"):
    if value == "":
        raise forms.ValidationError("%(field)s Cannot be empty" % {"field": field_name})


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
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of Course",
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-3 "
                "focus:outline-none focus:border-blue-700",
            }
        ),
    )

    course_code = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Code",
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-1 "
                "focus:outline-none focus:border-blue-700",
            }
        ),
    )

    professor = forms.CharField(
        required=False,
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
        required=False,
        validators=[validate_field_not_empty],
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write your review",
                "class": "w-full border border-gray-300 rounded-md py-2 px-3 my-1 "
                "focus:outline-none focus:border-blue-700",
            }
        ),
        help_text="Obscene language is not accepted. Please be kind, polite, and constructive in your review.",
    )

    def clean_course_name(self):
        course = self.cleaned_data["course_name"]

        validate_field_not_empty(course, field_name="Course")

        return course

    def clean_course_code(self):
        code = self.cleaned_data["course_code"]

        validate_field_not_empty(code, field_name="Course Code")

        return code

    def clean_professor(self):
        prof = self.cleaned_data["professor"]

        validate_field_not_empty(prof, field_name="Professor")
        return prof

    def clean_feedback_text(self):
        txt = self.cleaned_data["feedback_text"]

        validate_field_not_empty(txt, field_name="Feedback")
        return txt
