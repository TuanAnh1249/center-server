from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('upload/',views.UploadFileView.as_view()),
]
