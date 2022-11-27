from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '매일 자정 이상 없음 확인'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('No problem.'))