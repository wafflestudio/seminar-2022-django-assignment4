from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = '현재 활동 중인 유저의 수 알림'

    def handle(self, *args, **options):
        active_users = User.objects.filter(is_active=True)
        number_of_active_users = active_users.count()
        print(timezone.now())
        print("Successfully count active user(s)")

        if number_of_active_users <= 1:
            self.stdout.write(self.style.SUCCESS('"%s" user is active' % number_of_active_users))
        else:
            self.stdout.write(self.style.SUCCESS('"%s" users are active' % number_of_active_users))

