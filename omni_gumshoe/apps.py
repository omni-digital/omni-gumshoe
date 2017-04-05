# -*- coding: utf-8
from django.apps import AppConfig


class OmniGumshoeConfig(AppConfig):
    name = 'omni_gumshoe'

    def ready(self):
        import omni_gumshoe.signals
