from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = '오늘의 날짜 표시'

    def handle(self, *args, **options):
       self.stdout.write(f"{timezone.now()}")
