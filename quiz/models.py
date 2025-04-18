from django.db import models

# Create your models here.


class Level(models.Model):
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type


class Question(models.Model):
    level = models.ForeignKey(Level, related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=150)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text
