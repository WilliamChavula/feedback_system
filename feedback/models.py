from django.db import models
from django.contrib.auth import get_user_model

AppUser = get_user_model()


class Feedback(models.Model):
    student = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    course_name = models.CharField(
        max_length=50, help_text="Specify the name of the course feedback for"
    )
    course_code = models.CharField(max_length=10, help_text="Specify course code")
    professor = models.CharField(max_length=100, help_text="Who teaches the course?")
    feedback_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self) -> str:
        return (
            f"course_name: {self.course_name} - course_code: {self.course_code}) "
            f"taught by professor: {self.professor}"
        )
