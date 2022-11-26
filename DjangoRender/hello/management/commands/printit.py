from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = '로그인한지 90일이 지난 유저 비활성화'

    def handle(self, *args, **options):
        qs = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=90))
        qs.update(is_active=False)
        self.stdout.write(self.style.SUCCESS('Successfully deactivated users "%d"' % qs.count()))