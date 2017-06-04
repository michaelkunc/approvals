from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Food Oasis LA API')

urlpatterns = [
    url(r'^orderapplications/$', views.OrderApplicationsList.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)
