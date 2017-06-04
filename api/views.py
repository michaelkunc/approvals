from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

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
            return queryset.exclude(status='approved')

# http://127.0.0.1:8000/orderapplications/approved/?approved=Y


class OrderApplicationsListApprovedYear(generics.ListAPIView):
    serializer_class = OrderApplicationsSerializer

    def get_queryset(self):
        queryset = OrderApplications.objects.all()
        year = self.request.query_params.get('year', None)
        month = self.request.query_params.get('month', None)
        status = self.request.query_params.get('approved', None)
        if year is None:
            return queryset.exclude(status='approved')
        elif month is None:
            return queryset.filter(updated_at__year=year)
        else:
            return queryset.filter(updated_at__year=year).filter(updated_at__month=month)

# http://127.0.0.1:8000/orderapplications/year/?year=2016&month=10

# start of aggregation


# class OrderApplicationsListCount(viewsets.ModelViewSet):
#     serializer_class = OrderApplicationsSerializer
#     queryset = OrderApplications.objects.all()

#     def get_queryset(self):
#         return OrderApplications.objects.annotate(
#             total_applications=Count('applications'))
