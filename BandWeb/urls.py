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
import views

intro = [
    url(r'^abstract/(?P<lang>[ce]n)/$', views.get_intro),
    url(r'^leader/(?P<lang>[ce]n)/list/$', views.get_leader_list),
    url(r'^leader/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_leader_detail),
    url(r'^conductor/(?P<lang>[ce]n)/list/$', views.get_conductor_list),
    url(r'^conductor/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_conductor_detail),
    url(r'^director/(?P<lang>[ce]n)/$', views.get_director),
    url(r'^instrument/(?P<lang>[ce]n)/$', views.get_instrument),
    url(r'^performer/(?P<lang>[ce]n)/(?P<instrument_id>[0-9]+)/$', views.get_performer_list),
    url(r'^performer/(?P<lang>[ce]n)/detail/(?P<id>[0-9]+)/$', views.get_performer_detail)
]

urlpatterns = [
    url(r'^richtext/media/upload/$', views.upload_media),
    url(r'^intro/', include(intro))
]
