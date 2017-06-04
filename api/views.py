from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from api.models import OrderApplications
from api.serializers import OrderApplicationsSerializer


class OrderApplicationsList(generics.ListAPIView):
    serializer_class = OrderApplicationsSerializer

    def get_queryset(self):
        return OrderApplications.objects.all()


class OrderApplicationsListApproved(APIView):
    renderer_classes = (JSONRenderer,)

    serializer_class = OrderApplicationsSerializer

    def get(self, request, format=None):
        queryset = OrderApplications.objects.all()
        status = self.request.query_params.get('approved', None)
        year = self.request.query_params.get('year', None)
        month = self.request.query_params.get('month', None)

        field_name = 'approved_applications'

        if status == 'Y' and year is not None and month is not None:
            queryset = queryset.filter(status='approved')
            queryset = queryset.filter(updated_at__year=year)
            queryset = queryset.filter(updated_at__month=month)
        elif year is not None and month is not None:
            queryset = queryset.filter(status='approved')
            queryset = queryset.filter(updated_at__year=year)
            queryset = queryset.filter(updated_at__month=month)
        elif year is not None:
            queryset = queryset.filter(status='approved')
            queryset = queryset.filter(updated_at__year=year)
        else:
            queryset = queryset.exclude(status='approved')
            field_name = 'denied_applications'

        application_count = queryset.count()
        content = {field_name: application_count}
        return Response(content)


# http://127.0.0.1:8000/orderapplications/status/?approved=Y&year=2016&month=10
