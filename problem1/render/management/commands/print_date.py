from django.core.management.base import BaseCommand, CommandError
from django.utils.dateformat import DateFormat
from datetime import datetime

class Command(BaseCommand):
    help = '현재 날짜를 출력'

    def handle(self, *args, **options):
        today = DateFormat(datetime.now()).format('Y년m월d일')
        self.stdout.write(self.style.SUCCESS(today))