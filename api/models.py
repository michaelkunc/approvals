from django.db import models
from django.contrib.postgres.fields import JSONField


class OrderApplications(models.Model):
    application_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=30)
    person_id = models.IntegerField()
    max_affordability_cents = models.IntegerField()
    max_affordability_currency = models.CharField(max_length=10)
    expiration_date = models.DateTimeField(
        null=True, auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    vehicle_reference_id = models.CharField(max_length=200)
    locked_application = JSONField()
    threatmetrix_session_id = models.CharField(max_length=200)
    partial_application = JSONField()


class Audit(models.Model):
    run_date = models.DateTimeField(auto_now_add=True)
    row_count = models.IntegerField()
    run_type = models.CharField(max_length=30)
