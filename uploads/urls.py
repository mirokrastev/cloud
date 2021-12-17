from django.urls import path, re_path, include
from rest_framework import routers
from uploads import views

app_name = 'uploads'

router = routers.DefaultRouter()
router.register('files', views.FileUploadViewSet)

urlpatterns = [
    path('api/stats', views.StatsView.as_view(), name='stats'),
    path('api/files/<int:id>/download', views.FileDownloadView.as_view(), name='download'),
    re_path('^api/', include(router.urls)),
]
