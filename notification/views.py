from django.shortcuts import redirect, render
from django.views.generic import View

from .models import Notification


class NotificationView(View):

    template_name = "pages/notification.html"

    def get(self, request, *args, **kwargs):
        response = render(request, self.template_name)
        self.updatenotifications(request, response)
        return response

    def updatenotifications(self, request, response, *args, **kwargs):
        request.user.notification.filter(seen=False).update(seen=True)


notification_view = NotificationView.as_view()


class DeleteNotification(View):
    def get(self, request, notification_id, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                notification = Notification.objects.get(id=notification_id)
            except Notification.DoesNotExist:
                notification = None
            if notification is not None:
                notification.delete()
        return redirect("/notification/")


delete_notification_view = DeleteNotification.as_view()
