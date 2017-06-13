"""
Test omni_gumshoe.signals
"""
from django.contrib.admin.models import LogEntry
from django.contrib.auth import user_logged_in
from django.test import RequestFactory, TestCase

from tests.factories import StaffUserFactory, SuperUserFactory, UserFactory


class TestLogAdminLogin(TestCase):
    def setUp(self):
        self.request = RequestFactory().get('/foo')

    def test_supeuser_create_log(self):
        """
        `log_superuser_login` should create a `LogEntry` when superusers login.
        """
        user = SuperUserFactory.create()
        self.request.user = user
        user_logged_in.send(
            sender=user.__class__,
            request=self.request,
            user=user,
        )

        self.assertTrue(LogEntry.objects.get())

    def test_staff_user_create_log(self):
        """
        `log_admin_login` should create a `LogEntry` when staff users login.
        """
        user = StaffUserFactory.create()
        self.request.user = user
        user_logged_in.send(
            sender=user.__class__,
            request=self.request,
            user=user,
        )

        self.assertTrue(LogEntry.objects.get())

    def test_user_does_not_create_log(self):
        """
        `log_superuser_login` should not create a  `LogEntry` when users login.
        """
        user = UserFactory.create()
        self.request.user = user
        user_logged_in.send(
            sender=user.__class__,
            request=self.request,
            user=user,
        )

        self.assertFalse(LogEntry.objects.count())
