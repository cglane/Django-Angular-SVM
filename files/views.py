from django.http import HttpResponse
from files.models import csvFile
from files.serializers import FileSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework import generics
from rest_framework import viewsets,views
from django.views.generic.edit  import CreateView
from SVM import predict
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
import csv


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class TrainData(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # predict.writeCSV()
    queryset = csvFile.objects.all().order_by('created')
    serializer_class = FileSerializer

class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    def put(self, request, filename, format=None):
        file_obj = request.FILES['file']
        serializer = FileSerializer(title='hello', csvFile=request.FILES)
        serializer.save()
        # do some stuff with uploaded file
        return Response(status=204)
