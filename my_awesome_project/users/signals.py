from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from notification.models import Notification

User = get_user_model()


def user_update_notification(sender, instance, created, *args, **kwargs):
    if not created:
        Notification.objects.create(
            to_user=instance, message="Profile has been updated"
        )


post_save.connect(user_update_notification, sender=User)
