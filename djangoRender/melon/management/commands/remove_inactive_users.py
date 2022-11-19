from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from datetime import timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = '로그인한지 5년이 지난 유저 삭제'

    def handle(self, *args, **options):
        qs = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=365*5))
        count = qs.count()*1
        qs.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted %d users' % count))
