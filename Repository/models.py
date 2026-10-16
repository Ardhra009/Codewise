from django.db import models

# Create your models here.
class  QuestionsDB(models.Model):
    title=models.CharField(max_length=200)
    Language_CHOICES=(
        ("python","Python"),
        ("java","Java"),
        ("javascript","Javascript")
    )
    language=models.CharField(max_length=100,choices=Language_CHOICES)
    DIFFICULTY_CHOICES=(
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )
    difficulty_level=models.CharField(max_length=100,choices=DIFFICULTY_CHOICES)
    topic=models.CharField(max_length=100)
    notes=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_activate=models.BooleanField(default=True)
