from django.urls import path

from .views import delete_notification_view, notification_view

app_name = "notification"
urlpatterns = [
    path("", view=notification_view, name="notification"),
    path(
        "del/<str:notification_id>",
        view=delete_notification_view,
        name="notificationdel",
    ),
]
