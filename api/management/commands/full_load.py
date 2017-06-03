from django.core.management.base import BaseCommand
from django.core import management
import csv

from api.models import OrderApplications


class Command(BaseCommand):
    help = 'ingests data into the db from csv (soon to be s3 bucket). This command will kill and fill the db.'

    def handle(self, *args, **options):

        # clears the tables
        # management.call_command('flush', verbosity=0, interactive=False)
        with open('../fair_code_challenge/csvs/order_applications.csv', 'r') as f:
            reader = csv.reader(f)
            for r in reader:
                self.stdout.write(r[0])
