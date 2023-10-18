from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "course_name",
        "course_code",
        "professor",
        "feedback_text",
        "date_added",
    )
