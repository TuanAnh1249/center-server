from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.views import APIView

router = routers.DefaultRouter()
router.register(r'model', views.FileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('upload', views.FileUploadView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]