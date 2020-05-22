from django.db import models
from django.contrib.auth.models import User


class Keyword(models.Model):
    name = models.CharField(max_length=20)
    user_submitted = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=99)
    user_submitted = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    retired = models.BooleanField(default=False)

    def __str__(self):
        return self.title
