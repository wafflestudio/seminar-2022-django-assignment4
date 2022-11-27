from django.core.management.base import BaseCommand
import datetime

class Command(BaseCommand):
    help = '오늘의 날짜 표시'

    def handle(self, *args, **options):
       self.stdout.write(f"{datetime.datetime.now()}")
