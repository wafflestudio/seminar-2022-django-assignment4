from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'test command!'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Hello, cronjob and commands!'))