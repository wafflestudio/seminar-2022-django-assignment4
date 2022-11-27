from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'print username'

    def handle(self, *args, **options):
        print('Hello LimSu! By cron.')
