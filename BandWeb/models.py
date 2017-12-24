# coding=utf-8
from django.db import models
from datetime import datetime
from django.utils.timezone import utc


def default_time_now():
    return datetime.utcnow().replace(tzinfo=utc)


class Musicale(models.Model):
    update = models.DateTimeField(u"发布时间", auto_now=True)
    primary_key = models.IntegerField(u'主键', primary_key=True, default=True)
    title_cn = models.CharField(u"中文标题", max_length=100, unique=True, default='')
    content_cn = models.TextField(u"中文内容", default='')
    title_en = models.CharField(u"英文标题", max_length=100, unique=True, default='')
    content_en = models.TextField(u"英文内容", default='')
    main_image = models.ImageField(u"主页图片", upload_to='musicale', default=True)

    def save(self, *args, **kwargs):
        super(Musicale, self).save(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.title_cn, self.title_en)

    class Meta:
        verbose_name = u'音乐会'
        verbose_name_plural = verbose_name
