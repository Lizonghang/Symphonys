# coding=utf-8
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ObjectDoesNotExist
from models import *
import json
import utils


@require_POST
def upload_media(request):
    media_type = request.GET.get('dir')
    media_data = request.FILES.get('file')
    manager = utils.UploadMediaManager()
    media_url = manager.save(media_type, media_data)
    return JsonResponse({'error': 0, 'url': media_url})


@require_GET
def get_intro(request, lang):
    obj = YueTuanIntro.objects.first()
    content = obj.get_abstract(lang)
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_leader_list(request, lang):
    content = {
        'president': [],
        'vice_president': []
    }
    for obj in YueTuanLeader.objects.all():
        obj_info = obj.get_abstract(lang, 'abstract')
        if obj_info['president_type'] == 0:
            content['president'].append(obj_info)
        else:
            content['vice_president'].append(obj_info)
    content.update(PresidentAddress.objects.first().get_abstract(lang))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_leader_detail(request, lang, id):
    obj = YueTuanLeader.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_conductor_list(request, lang):
    content = []
    for obj in Conductor.objects.all():
        content.append(obj.get_abstract(lang, 'abs'))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_conductor_detail(request, lang, id):
    obj = Conductor.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_director(request, lang):
    obj = Director.objects.first()
    content = obj.get_abstract(lang)
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_instrument(request, lang):
    content = [obj.get_abstract(lang) for obj in InstrumentType.objects.all()]
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_performer_list(request, lang, instrument_id):
    content = []
    for obj in Performer.objects.filter(instrument_type=InstrumentType.objects.get(id=instrument_id)):
        content.append(obj.get_abstract(lang, 'abstract'))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_performer_detail(request, lang, id):
    obj = Performer.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})
