from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = '로그인 한지 1년 지난 유저 비 활성화 및 현재 활성화 된 유저의 수 출력'

    def handle(self, *args, **options):
        user_disable = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=365))
        user_disable.update(is_active=False)
        user_num = User.objects.filter(is_active=True).count()
        self.stdout.write(self.style.SUCCESS('User update Success! The number of Remain users is "%d"') % user_num)
