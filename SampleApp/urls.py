from django.urls import path

from . import views
from SampleProject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/',views.details, name='details'),
    path('create',views.create, name='create'),
    path('fileupload',views.fileupload, name='fileupload'),
    path('bulk-file-upload', views.bulk_file_upload, name='bulk-file-upload'),
]
