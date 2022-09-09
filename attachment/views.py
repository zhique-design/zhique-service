from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from ZhiQue import permissions
from .models import Attachment
from .storage import attachment_storage


class AttachmentUploadView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, version):
        try:
            file = request.FILES['file']
        except MultiValueDictKeyError:
            raise ValidationError('参数错误')
        name = attachment_storage.save(file.name, file)
        attachment = get_object_or_404(Attachment, file_name=name)
        return JsonResponse({'download_url': attachment.get_url(request)}, status=status.HTTP_201_CREATED)


class AttachmentDownloadView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, version, attachment_id=None):
        attachment = attachment_storage.open(attachment_id)
        response = HttpResponse(attachment, content_type=attachment.mimetype)
        response['Content-Disposition'] = 'attachment;filename={name}'.format(name=attachment.filename).encode('utf-8')
        return response