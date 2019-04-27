import csv
from django.core.management.base import BaseCommand, CommandError
from discounts.models import Discount


class Command(BaseCommand):
    help = 'Load discount model with provided csv content'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        parser.add_argument('--d', help='Delete previous discounts', action="store_true")

    def handle(self, *args, **options):
        path = options['path']
        if options['d']:
            Discount.objects.all().delete()

        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Discount.objects.get_or_create(
                    code=row[0],
                )
                if created:
                    self.stdout.write(self.style.SUCCESS('discount added "%s"' % row[0]))
