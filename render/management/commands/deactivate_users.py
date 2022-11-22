from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = '3개월이 지난 유저들에게 비밀번호 변경 메일 전송'

    def handle(self, args, **options):
        qs = User.objects.filter(last_login__lt=timezone.now() - timedelta(months=3))
        for user in qs:
            user.email_user("Change your password", "Please change you password")
        self.stdout.write(self.style.SUCCESS('Successfully sent mails to users "%d"' % qs.count()))