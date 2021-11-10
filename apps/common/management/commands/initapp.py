from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.apps import apps
from django.contrib import admin
from apps.common.models.base import load_initial_data


class Command(BaseCommand):
    help = "Initializes the app by running the necessary commands."

    def handle(self, *args, **kwargs):
        """Call all the necessary commands."""
        call_command("migrate")

        models = apps.get_models()
        for model in models:
            try:
                load_initial_data(model)
            except Exception as e:
                # print(model.__name__)
                # print(e)
                continue
