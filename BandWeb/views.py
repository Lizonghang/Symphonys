# coding=utf-8
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ObjectDoesNotExist
import json
import utils


@require_POST
def upload_media(request):
    media_type = request.GET.get('dir')
    media_data = request.FILES.get('file')
    manager = utils.UploadMediaManager()
    media_url = manager.save(media_type, media_data)
    return JsonResponse({'error': 0, 'url': media_url})
