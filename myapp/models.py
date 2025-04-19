from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=255)
    request_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)  # Indicates whether the request has been processed


    def __str__(self):
        return self.user.username

