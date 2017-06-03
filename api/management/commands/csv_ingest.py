from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = 'ingests data into the db from csv (soon to be s3 bucket). This command will kill and fill the db.'

    def handle(self, *args, **options):
        self.stdout.write('Testing the command')
