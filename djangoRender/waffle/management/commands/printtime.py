from django.core.management.base import BaseCommand
from datetime import datetime


class Command(BaseCommand):
    help = '현재 시간 프린트'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('The time now is %s' % datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")))
