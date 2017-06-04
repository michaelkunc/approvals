from rest_framework import serializers
from api.models import OrderApplications


class OrderApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderApplications
        fields = ('application_id', 'status', 'updated_at')
