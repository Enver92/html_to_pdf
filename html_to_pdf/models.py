from django.conf import settings
from django.db import models

# Create your models here.
class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answers',
                                blank=True, null=True, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=255)
    value = models.TextField()
    index = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.question_name
