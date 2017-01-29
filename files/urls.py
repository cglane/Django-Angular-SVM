from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^files/', views.index, name='hello'),
    # url(r'^api/train_data$', views.TrainData.asView()),
    url(r'^upload/(?P<filename>[^/]+)$', csrf_exempt(views.FileUploadView.as_view()))
]
urlpatterns = format_suffix_patterns(urlpatterns)
