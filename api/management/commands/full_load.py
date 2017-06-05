from django.core.management.base import BaseCommand
from django.core import management
import csv
import boto3

from api.models import OrderApplications, Audit


class Command(BaseCommand):
    help = """Performs a full load of data into the db from the S3 bucket.
    			This command will kill and fill the db."""

    def handle(self, *args, **options):

        self._clear_data()
        # self._get_data_from_s3() ##need to get my aws credentials into the
        # heroku env
        row_count = 0
        with open('csvs/order_applications.csv') as f:
            reader = csv.reader(f)
            next(f)
            for r in reader:
                order_app = OrderApplications(
                    application_id=r[0],
                    status=r[1],
                    person_id=r[2],
                    max_affordability_cents=r[3],
                    max_affordability_currency=r[4],
                    created_at=r[6],
                    updated_at=r[7],
                    vehicle_reference_id=r[8],
                    locked_application=r[9],
                    threatmetrix_session_id=r[10],
                    partial_application=r[11])
                order_app.save()
                row_count += 1
            self.stdout.write(
                "{0} rows have been loaded to the database".format(row_count))

            self._update_audit_table(row_count, 'Full Load')

    def _clear_data(self):
        OrderApplications.objects.all().delete()

    def _update_audit_table(self, row_count, run_type):
        Audit(row_count=row_count, run_type=run_type).save()
        self.stdout.write('The audit table has been updated.')

    def _get_data_from_s3(self):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('coding-challenge-1')
        s3.meta.client.download_file(
            bucket.name, 'order_applications.csv', 'csvs/order_applications.csv')
