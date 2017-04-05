from django.contrib.admin.models import LogEntry
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

LOGIN = 4


@receiver(user_logged_in)
def log_superuser_login(request, user, **kwargs):
    """
    When a `user_logged_in` signal is received create a LogEntry is the
    user is a superuser.

    :param request: Request object
    :param user: User object
    :param kwargs:
    """
    if user.is_superuser:
        LogEntry.objects.create(
            user=user,
            action_flag=LOGIN,
            change_message='{} logged in to {}'.format(user, request.path),
        )
