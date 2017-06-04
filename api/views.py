from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from api.models import OrderApplications
from api.serializers import OrderApplicationsSerializer


class OrderApplicationsList(generics.ListAPIView):
    serializer_class = OrderApplicationsSerializer

    def get_queryset(self):
        queryset = OrderApplications.objects.all()
        return queryset
