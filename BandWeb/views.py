# coding=utf-8
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.core.paginator import Paginator, EmptyPage
from models import *
import math
import utils


@require_POST
def upload_media(request):
    media_type = request.GET.get('dir')
    media_data = request.FILES.get('file')
    manager = utils.UploadMediaManager()
    media_url = manager.save(media_type, media_data)
    return JsonResponse({'error': 0, 'url': media_url})


@require_GET
def get_banner(request, lang):
    content = []
    for obj in Banner.objects.order_by('order'):
        content.append(obj.get_abstract(lang))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_home_news(request, lang):
    content = {'festival': [], 'business': []}
    for obj in MusicFestival.objects.order_by('-id')[:3]:
        content['festival'].append(obj.get_abstract(lang, 'abstract'))
    for obj in BusinessDynamics.objects.order_by('-id')[:3]:
        content['business'].append(obj.get_abstract(lang, 'abstract'))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def view_musicale_detail(request, lang, id):
    obj = Musicale.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def view_musicale_list(request, lang, page):
    musicale_list = Musicale.objects.order_by('-id')
    paginator = Paginator(musicale_list, 6)
    try:
        musicale_list = paginator.page(int(page))
    except EmptyPage:
        musicale_list = paginator.page(paginator.num_pages)
    content = {'news': []}
    for obj in musicale_list:
        content['news'].append(obj.get_abstract(lang, 'abstract'))
    content['max_page'] = paginator.num_pages
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def view_musicfestival_detail(request, lang, id):
    obj = MusicFestival.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def view_musicfestival_list(request, lang, page):
    musicfestival_list = MusicFestival.objects.order_by('-id')
    paginator = Paginator(musicfestival_list, 6)
    try:
        musicfestival_list = paginator.page(int(page))
    except EmptyPage:
        musicfestival_list = paginator.page(paginator.num_pages)
    content = {'news': []}
    for obj in musicfestival_list:
        content['news'].append(obj.get_abstract(lang, 'abstract'))
    content['max_page'] = paginator.num_pages
    return JsonResponse({'error': 0, 'body': content})


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

"""
@require_GET
def get_beautymelody_intro(request, lang, verbose):
    obj = BeautyMelodyIntro.objects.first()
    content = obj.get_abstract(lang, verbose)
    return JsonResponse({'error': 0, 'body': content})
"""


@require_GET
def get_beautymelody_news_list(request, lang, page):
    content = {'news': []}
    for obj in BeautyMelodyNews.objects.order_by('-id')[(int(page)-1)*5:int(page)*5]:
        content['news'].append(obj.get_abstract(lang, 'abstract'))
    content['max_page'] = int(math.ceil(BeautyMelodyNews.objects.count()/5.0))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_beautymelody_news_detail(request, lang, id):
    obj = BeautyMelodyNews.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})

"""
@require_GET
def get_opera_intro(request, lang, verbose):
    obj = OperaIntro.objects.first()
    content = obj.get_abstract(lang, verbose)
    return JsonResponse({'error': 0, 'body': content})
"""


@require_GET
def get_opera_news_list(request, lang, page):
    content = {'news': []}
    for obj in OperaNews.objects.order_by('-id')[(int(page)-1)*5:int(page)*5]:
        content['news'].append(obj.get_abstract(lang, 'abstract'))
    content['max_page'] = int(math.ceil(OperaNews.objects.count()/5.0))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_opera_news_detail(request, lang, id):
    obj = OperaNews.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_businessdynamics_news_list(request, lang, page, order):
    content = {'news': []}
    order_map = {'sequence': 'id', 'reverse': '-id'}
    for obj in BusinessDynamics.objects.order_by(order_map[order])[(int(page)-1)*5:int(page)*5]:
        content['news'].append(obj.get_abstract(lang, 'abstract'))
    content['max_page'] = int(math.ceil(BusinessDynamics.objects.count()/5.0))
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def get_businessdynamics_news_detail(request, lang, id):
    obj = BusinessDynamics.objects.get(id=id)
    content = obj.get_abstract(lang, 'detail')
    return JsonResponse({'error': 0, 'body': content})


@require_GET
def search(request):
    return JsonResponse({'error': 1, 'code': 0, 'msg': 'Under Development'})


def request500_error(request):
    return JsonResponse({'error': 1, 'code': 500, 'msg': 'Invalid Operation'})


def request404_error(request):
    return JsonResponse({'error': 1, 'code': 404, 'msg': 'Invalid Path'})
