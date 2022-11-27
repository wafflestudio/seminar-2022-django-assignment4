import datetime
from typing import Any, Optional

from django.core.management import base


class Command(base.BaseCommand):
    help = """
        Test Management Command with Cron Job.
        Output message is a kind of greeting with current time data.
        If you give name as input args, greeting gets more detailed.
    """

    def add_arguments(self, parser: base.CommandParser) -> None:
        parser.add_argument('--name', type=str)
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        name = options.get("name", None)
        self.stdout.write(
            f"""
            Hello, {name if name else "Everyone"}.
            Today is {datetime.datetime.now()}.
            Nice to meet you!
            """
        )
