# from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        read_notifications = request.user.notification.filter(seen=True)
        unread_notifications = request.user.notification.filter(seen=False)
        return {
            "read_notifications": read_notifications,
            "unread_notifications": unread_notifications,
        }
    else:
        return {"read_notifications": [], "unread_notifications": []}
