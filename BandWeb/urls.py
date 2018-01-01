"""Symphonys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
import BandWeb.views as views

intro = [
    url(r'^intro/(?P<lang>[ce]n)/$', views.get_intro),
    url(r'^leader/(?P<lang>[ce]n)/list/$', views.get_leader_list),
    url(r'^leader/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_leader_detail),
    url(r'^conductor/(?P<lang>[ce]n)/list/$', views.get_conductor_list),
    url(r'^conductor/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_conductor_detail),
    url(r'^director/(?P<lang>[ce]n)/list/$', views.get_director_list),
    url(r'^director/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_director_detail),
    url(r'^instrument/(?P<lang>[ce]n)/$', views.get_instrument),
    url(r'^performer/(?P<lang>[ce]n)/list/(?P<instrument_id>[0-9]+)/$', views.get_performer_list),
    url(r'^performer/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_performer_detail),
]

home = [
    url(r'^banner/(?P<lang>[ce]n)/list/$', views.get_banner),
    url(r'^news/(?P<lang>[ce]n)/list/$', views.get_home_news)
]

musicale = [
    url(r'^musicale/(?P<lang>[ce]n)/list/(?P<page>[0-9]+)/$', views.view_musicale_list),
    url(r'^musicale/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.view_musicale_detail),
    url(r'^festival/(?P<lang>[ce]n)/list/(?P<page>[0-9]+)/$', views.view_musicfestival_list),
    url(r'^festival/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.view_musicfestival_detail)
]

beautymelody = [
    # url(r'^intro/(?P<lang>[ce]n)/(?P<verbose>[abstrcdeil]+)/$', views.get_beautymelody_intro),
    url(r'^news/(?P<lang>[ce]n)/list/(?P<page>[0-9]+)/$', views.get_beautymelody_news_list),
    url(r'^news/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_beautymelody_news_detail)
]

opera = [
    # url(r'^intro/(?P<lang>[ce]n)/(?P<verbose>[abstrcdeil]+)/$', views.get_opera_intro),
    url(r'^news/(?P<lang>[ce]n)/list/(?P<page>[0-9]+)/$', views.get_opera_news_list),
    url(r'^news/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_opera_news_detail)
]

businessdynamics = [
    url(r'^news/(?P<lang>[ce]n)/list/(?P<order>[sequncrv]+)/(?P<page>[0-9]+)/$', views.get_businessdynamics_news_list),
    url(r'^news/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_businessdynamics_news_detail)
]

urlpatterns = [
    url(r'^richtext/media/upload/$', views.upload_media),
    url(r'^search/$', views.search),
    url(r'^home/', include(home)),
    url(r'^intro/', include(intro)),
    url(r'^beautymelody/', include(beautymelody)),
    url(r'^opera/', include(opera)),
    url(r'^businessdynamics/', include(businessdynamics)),
    url(r'^musicale/', include(musicale))
]
