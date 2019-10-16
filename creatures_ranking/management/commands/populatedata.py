from django.core.management.base import BaseCommand, CommandError
from ._private import create_castles,create_creatures


class Command(BaseCommand):
    help = 'Populates database with creatures and castles'

    def handle(self, *args, **options):
        create_castles()
        self.stdout.write(self.style.SUCCESS("Succesfully create castles"))
        create_creatures()
        self.stdout.write(self.style.SUCCESS("Succesfully created creatures"))