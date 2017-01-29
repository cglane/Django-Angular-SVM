from django.conf.urls import patterns, include, url
from Finances.views import IndexView,UserViewSet,GroupViewSet
from django.contrib import admin
from files.models import csvFile
from files.views import TrainData
from rest_framework import routers
class csvAdmin(admin.ModelAdmin):
      list_display    = ['isPrimary','title', 'comment', 'csvFile']

admin.site.register(csvFile, csvAdmin)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'train_data', TrainData)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('files.urls')),
    url(r'^$', IndexView.as_view(), name='index'),

)
