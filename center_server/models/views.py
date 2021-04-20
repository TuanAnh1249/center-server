from .models import File
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FileSerializer

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from . import views
# class FileUploadView(views.APIView):
#     parser_classes = [FileUploadParser]

#     def put(self, request, filename, format=None):
#         file_obj = request.data['file']
#         # ...
#         # do some stuff with uploaded file
#         # ...
#         return Response(file_obj)

class FileUploadView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(['POST'])
    @parser_classes([FormParser, MultiPartParser])
    def example_view(request, format=None):
        """
        A view that can accept POST requests with JSON content.
        """
        return Response({'received data': request.data})

    
class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

# class ModelViewSet(viewsets.ModelViewSet):
#     queryset = File.objects.all().order_by('version')
#     serializer_class = FileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [FormParser, MultiPartParser]

#     # logger.error('================================', get_devices.delay())
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['username', 'ip',
#     #                     'agentInstalled', 'mac_addr', 'tracing_syscall', 'id']
#     @extend_schema(
#             parameters=[
#             ],
#             # request=UpdateIPFrequencySerializer,
#             responses=FileSerializer,
#         )
#         @action(detail=False, methods=['patch'])
#         def upload(self, request):
#             try:
#                 current_device = Devices.objects.filter(
#                     ip=request.data['ip']).first()
#                 if (current_device.ips == []):
#                     current_device.ips = {}
#                 for ip in request.data['list_ip']:
#                     print(ip)
#                     # Check trường hợp mặc định là [] -> đổi sang dict
#                     #  update tần suất
#                     if not (ip in current_device.ips):
#                         current_device.ips[ip] = 1
#                     else:
#                         current_device.ips[ip] = current_device.ips[ip] + 1
#                 current_device.save()
#                 return Response(DevicesSerializer(current_device).data)
#             except Exception as e:
#                 logging.error(e)
#                 return Response(data={'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)
