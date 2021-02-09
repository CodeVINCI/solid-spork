from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.


class Notification(models.Model):
    to_user = models.ForeignKey(
        User, related_name="notification", on_delete=models.CASCADE
    )
    message = models.CharField(max_length=250, blank=False, null=False)
    seen = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
