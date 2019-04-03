from django.core.management.base import BaseCommand

from ...service import write_led_light_data


class Command(BaseCommand):
    help = 'Run background service Scheduler'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Running service functions...')
        write_led_light_data()
        self.stdout.write(self.style.SUCCESS('Service done'))
