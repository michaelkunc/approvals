from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from api.models import OrderApplications
from api.serializers import OrderApplicationsSerializer


class OrderApplicationsList(generics.ListAPIView):
    serializer_class = OrderApplicationsSerializer

    def get_queryset(self):
        return OrderApplications.objects.all()


class OrderApplicationsListApproved(generics.ListAPIView):
    serializer_class = OrderApplicationsSerializer

    def get_queryset(self):
        queryset = OrderApplications.objects.all()
        status = self.request.query_params.get('approved', None)
        if status == 'Y':
            return queryset.filter(status='approved')
        else:
            return queryset

# http://127.0.0.1:8000/orderapplications/approved/?approved=Y


class OrderApplicationsListApprovedYear(generics.ListAPIView):
    serializer_class = OrderApplicationsSerializer

    def get_queryset(self):
        queryset = OrderApplications.objects.all()
        year = self.request.query_params.get('year', None)
        if year is None:
            return queryset
        else:
            return queryset.filter(updated_at__year=year)

# http://127.0.0.1:8000/orderapplications/year/?year=2017
