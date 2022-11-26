from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone


class Command(BaseCommand):
    help = 'Deactivate dormant account. (No visit record more than 30 days.)'

    def handle(self, *args, **options):
        queryset = User.objects.filter(last_login__lt=timezone.now() - timezone.timedelta(days=30))
        queryset.update(is_active=False)
        self.stdout.write(self.style.SUCCESS(f'Deactivated {queryset.count()} dormant accounts.'))