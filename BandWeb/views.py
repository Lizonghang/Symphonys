# coding=utf-8
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ObjectDoesNotExist
import json
import utils
from django.core.paginator import Paginator
from BandWeb.models import *
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers


@require_POST
def upload_media(request):
    media_type = request.GET.get('dir')
    media_data = request.FILES.get('file')
    manager = utils.UploadMediaManager()
    media_url = manager.save(media_type, media_data)
    return JsonResponse({'error': 0, 'url': media_url})


def view_musicale_list(request):
    musicale_list = Musicale.objects.all()
    paginator = Paginator(musicale_list, 3)
    page = request.GET.get('page')
    try:
        musicale_list = paginator.page(page)
    except PageNotAnInteger:
        musicale_list = paginator.page(1)
    except EmptyPage:
        musicale_list = paginator.page(paginator.num_pages)
    content = {
        'musicale_list': musicale_list,
        'title_cn': Musicale.title_cn,
        'update': Musicale.update,
        'main_image': Musicale.main_image,
    }
    return JsonResponse(serializers.serialize(content), safe=False)


def view_musicale_detail(request):
    primary_key = request.GET.get('primary_key')
    if primary_key == '':
        return HttpResponseRedirect(reverse('view_musicale_list'))
    try:
        musicale = Musicale.objects.get(pk=primary_key)
    except Musicale.DoesNotExist:
        return HttpResponseRedirect(reverse('view_musicale_list'))
    content = {
        'title_cn': musicale.title_cn,
        'content_cn': musicale.content_cn,
        'title_en': musicale.title_en,
        'content_en': musicale.content_en,
    }
    return JsonResponse(serializers.serialize(content), safe=False)
