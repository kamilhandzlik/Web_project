from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    create_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resetowanie hasła dla użytkownika {self.user.username} w dniu {self.create_when}"


class RegistrationConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_id = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)