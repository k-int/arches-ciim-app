from django.apps import AppConfig
from django.conf import settings


class ArchesCiimAppConfig(AppConfig):
    name = "arches_ciim_app"
    verbose_name = "Arches CIIM App"
    is_arches_application = True
