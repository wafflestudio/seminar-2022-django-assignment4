from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = '마지막 접속 후 1년 지난 사용자를 휴면 처리'

    def handle(self, *args, **options):
        qs = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=365))
        for user in qs:
            user.email_user('휴면 처리', '마지막으로 접속한지 1년이 경과되어 휴면 처리되었습니다.')
        qs.update(is_active=False)
        self.stdout.write(self.style.SUCCESS('Successfully deactivated users "%d"' % qs.count()))