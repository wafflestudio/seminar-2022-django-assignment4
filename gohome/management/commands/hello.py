from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = 'Displays hello.'

    def handle(self, *args, **options):
        self.stdout.write("Hello")
