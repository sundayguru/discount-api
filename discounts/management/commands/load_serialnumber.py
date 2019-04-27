import csv

from django.core.management.base import BaseCommand

from discounts.models import SerialNumber


class Command(BaseCommand):
    help = 'Load serial number model with provided csv content'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        parser.add_argument(
            '--d', help='Delete previous serial numbers', action="store_true"
        )

    def handle(self, *args, **options):
        path = options['path']
        if options['d']:
            SerialNumber.objects.all().delete()

        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = SerialNumber.objects.get_or_create(
                    serial=row[0],
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS('serial number added "%s"' % row[0])
                    )
