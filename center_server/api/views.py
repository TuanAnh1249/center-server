from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import TaskSerializer, FileExampleSerializer
from rest_framework import permissions, generics

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser

# Create your views here.
@api_view(['GET'])
def  api_overview(request):
    api_urls = {
        'List':'task-list',
        'Detail view': 'task-detail/<str:pk>/',
        'Create' : 'task-create',
        'Update' : 'task-update/<str:pk>',
        'Delete' : 'task-delete/<str:pk>'
    }
    # data = {"response":"ok"}
    return Response(api_urls)


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileExampleSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = (FormParser, MultiPartParser)
    # avatar = openapi.Parameter('avatar',openapi.IN_QUERY, description='custom param',  type=openapi.TYPE_FILE)
  
    def post(self,request,*args,**kwargs):
        print("logging from image _ post")
        print(request.data)           
        return self.create(request,*args,**kwargs)