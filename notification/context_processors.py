# from .models import Notification


class Notification_context:
    def read_notifications(self, request):
        user = request.user
        return user.notification.filter(seen=True)

    def unread_notifications(self, request):
        return request.user.notification.filter(seen=False)

    def get(self, request):
        if not request.user.is_authenticated:
            return {"read_notifications": [], "unread_notifications": []}
        read_notify = self.read_notifications(request)
        unread_notify = self.unread_notifications(request)
        response_object = {
            "read_notifications": read_notify,
            "unread_notifications": unread_notify,
        }
        return response_object


def notifications(request):
    return Notification_context().get(request)
