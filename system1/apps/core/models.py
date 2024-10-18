from django.db import models
from django.contrib.auth.models import User


class Users(User):
    created_at = models.DateTimeField(
        auto_now_add=True
    ) 
    def __str__(self):
        return self.username
