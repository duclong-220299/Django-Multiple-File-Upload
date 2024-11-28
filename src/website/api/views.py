from rest_framework.response import Response
from django.views.generic import DeleteView
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser


from django.views.decorators.csrf import csrf_exempt

from .serializers import *
from ..models import *


class PhotoModelViewSet(viewsets.ModelViewSet):

    serializer_class = PhotoSerializer
    parser_classes = [MultiPartParser]

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if "file" not in request.FILES or not serializer.is_valid():
            return Response(
                {"details": "there is an issue with uploaded files"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for file in request.FILES.getlist("file"):
            Photo.objects.create(file=file)

        return Response(
            {"details": "uploaded successfully"}, status=status.HTTP_201_CREATED
        )


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = "website/photo_confirm_delete.html"
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.file.delete()
        return super().delete(request, *args, **kwargs)
