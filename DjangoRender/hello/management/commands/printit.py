from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = '인사합니다'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Hello, Have a nice day!'))