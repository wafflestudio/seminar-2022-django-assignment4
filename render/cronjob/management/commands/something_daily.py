from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = '가입한지 100일 된 유저들의 등급 올려주기'

    def handle(self, *args, **options):
        gs = User.objects.filter(date_joined=100)
        gs.update(is_staff=True)
        self.stdout.write(self.style.SUCCESS('Successfully :가입한지 100일 된 유저들의 등급 올려주기'))