from django.core.management.base import BaseCommand

from ...scheduler import Scheduler


class Command(BaseCommand):
    help = 'Run background service Scheduler'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS('Successfully started Scheduler'))
