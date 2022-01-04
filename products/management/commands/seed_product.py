# python import
# django import
from django.core.management.base import BaseCommand
# third party import
from django_seed import Seed
# local import
from ...models import Product


class Command(BaseCommand):
    hel = 'this command creates users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="How many products do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(Product, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} product created!'))