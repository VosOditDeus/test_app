from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message
