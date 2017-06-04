from django.core.management.base import BaseCommand
from django.core import management
import csv

from api.models import OrderApplications


class Command(BaseCommand):
    help = """Performs a full load of data into the db from csv (soon to be s3 bucket).
    			This command will kill and fill the db."""

    def handle(self, *args, **options):

        # clears the tables
        # management.call_command('flush', verbosity=0, interactive=False)
        row_count = 0
        # try:
        with open('../fair_code_challenge/csvs/order_applications.csv', 'r') as f:
            reader = csv.reader(f)
            next(f)
            for r in reader:
                # print(r[7])
                order_app = OrderApplications(application_id=r[0],
                                              status=r[1],
                                              person_id=r[2],
                                              max_affordability_cents=r[
                                                  3],
                                              max_affordability_currency=r[
                                                  4],
                                              # expiration_date=r[5],
                                              created_at=r[6],
                                              updated_at=r[7],
                                              vehicle_reference_id=r[8],
                                              locked_application=r[9],
                                              threatmetrix_session_id=r[
                                                  10],
                                              partial_application=r[11])
                order_app.save()
                row_count += 1
            self.stdout.write(
                "{0} rows have been loaded to the database".format(row_count))

            # r5 and r8 are empty
