from django.contrib.admin.models import CHANGE, LogEntry
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def log_admin_login(request, user, **kwargs):
    """
    When a `user_logged_in` signal is received create a LogEntry is the
    user is a superuser.

    :param request: Request object
    :param user: User object
    :param kwargs:
    """
    if user.is_staff or user.is_superuser:
        LogEntry.objects.create(
            user=user,
            action_flag=CHANGE,
            change_message='{} logged in to {}'.format(user, request.path),
        )
