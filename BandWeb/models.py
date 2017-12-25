# coding=utf-8
import config
from django.db import models


class Musicale(models.Model):
    update = models.DateTimeField(u"发布时间", auto_now=True)
    title_cn = models.CharField(u"中文标题", max_length=100, unique=True, default='')
    content_cn = models.TextField(u"中文内容", default='')
    title_en = models.CharField(u"英文标题", max_length=100, unique=True, default='')
    content_en = models.TextField(u"英文内容", default='')

    def save(self, *args, **kwargs):
        super(Musicale, self).save(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.title_cn, self.title_en)

    class Meta:
        verbose_name = u'音乐会'
        verbose_name_plural = verbose_name


class YueTuanIntro(models.Model):
    content_cn = models.TextField(u"乐团介绍(中文)", default='')
    content_en = models.TextField(u"乐团介绍(英文)", default='')

    def get_abstract(self, lang='cn'):
        if lang == 'cn':
            return {'content_cn': self.content_cn}
        else:
            return {'content_en': self.content_en}

    def save(self, *args, **kwargs):
        nb = YueTuanIntro.objects.count()
        if nb == 0 or (nb == 1 and self.id):
            super(YueTuanIntro, self).save(*args, **kwargs)

    def __str__(self):
        return u'乐团介绍'

    class Meta:
        verbose_name = u'乐团介绍'
        verbose_name_plural = verbose_name


class YueTuanLeader(models.Model):
    president_img = models.ImageField(u"团长头像", upload_to='image', default=None)
    president_type = models.CharField(u"正副级", max_length=20, default=u'团长', choices=(('0', u'团长'), ('1', u'副团长')))
    president_name_cn = models.CharField(u"团长名称(中文)", max_length=20, default='')
    president_intro_cn = models.CharField(u"团长简介(中文)", max_length=50, default='')
    president_detail_cn = models.TextField(u"团长介绍详情(中文)", default='')
    president_name_en = models.CharField(u"团长名称(英文)", max_length=20, default='')
    president_intro_en = models.CharField(u"团长简介(英文)", max_length=50, default='')
    president_detail_en = models.TextField(u"团长介绍详情(英文)", default='')

    def get_abstract(self, lang, verbose):
        intro = {
            'id': self.id,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.president_img.url),
            'president_type': int(self.president_type)
        }
        if lang == 'cn':
            intro['name'] = self.president_name_cn
            intro['intro'] = self.president_intro_cn
            if verbose == 'detail':
                intro['detail'] = self.president_detail_cn
        else:
            intro['name'] = self.president_name_en
            intro['intro'] = self.president_intro_en
            if verbose == 'detail':
                intro['detail'] = self.president_detail_en
        return intro

    def __str__(self):
        return self.president_name_cn

    class Meta:
        verbose_name = u'乐团团长'
        verbose_name_plural = verbose_name


class PresidentAddress(models.Model):
    address_cn = models.TextField(u"团长致辞(中文)", default='')
    address_en = models.TextField(u"团长致辞(英文)", default='')

    def get_abstract(self, lang):
        if lang == 'cn':
            return {'address': self.address_cn}
        else:
            return {'address': self.address_en}

    def save(self, *args, **kwargs):
        nb = PresidentAddress.objects.count()
        if nb == 0 or (nb == 1 and self.id):
            super(PresidentAddress, self).save(*args, **kwargs)

    def __str__(self):
        return u'团长致辞'

    class Meta:
        verbose_name = u'团长致辞'
        verbose_name_plural = verbose_name


class Conductor(models.Model):
    img = models.ImageField(u"头像", upload_to='image', default=None)
    name_cn = models.CharField(u"名称(中文)", max_length=20, default='', unique=True)
    intro_cn = models.CharField(u"简介(中文)", max_length=50, default='')
    detail_cn = models.TextField(u"介绍详情(中文)", default='')
    name_en = models.CharField(u"名称(英文)", max_length=20, default='', unique=True)
    intro_en = models.CharField(u"简介(英文)", max_length=50, default='')
    detail_en = models.TextField(u"介绍详情(英文)", default='')

    def get_abstract(self, lang, verbose):
        if lang == 'cn':
            intro = {
                'id': self.id,
                'img': "{proto}://{domain}{path}".format(
                    proto=config.PROTOCOL,
                    domain=config.DOMAIN,
                    path=self.img.url
                ),
                'name': self.name_cn,
                'intro': self.intro_cn
            }
            if verbose == 'detail':
                intro['detail'] = self.detail_cn
            return intro
        else:
            intro = {
                'id': self.id,
                'img': "{proto}://{domain}{path}".format(
                    proto=config.PROTOCOL,
                    domain=config.DOMAIN,
                    path=self.img.url
                ),
                'name': self.name_en,
                'intro': self.intro_en
            }
            if verbose == 'detail':
                intro['detail'] = self.detail_en
            return intro

    def __str__(self):
        return self.name_cn

    class Meta:
        verbose_name = u'驻团指挥'
        verbose_name_plural = verbose_name


class Director(models.Model):
    img = models.ImageField(u"头像", upload_to='image', default=None)
    name_cn = models.CharField(u"名称(中文)", max_length=20, default='')
    intro_cn = models.CharField(u"简介(中文)", max_length=50, default='')
    detail_cn = models.TextField(u"介绍详情(中文)", default='')
    name_en = models.CharField(u"名称(英文)", max_length=20, default='')
    intro_en = models.CharField(u"简介(英文)", max_length=50, default='')
    detail_en = models.TextField(u"介绍详情(英文)", default='')

    def get_abstract(self, lang):
        if lang == 'cn':
            return {
                'img': "{proto}://{domain}{path}".format(
                    proto=config.PROTOCOL,
                    domain=config.DOMAIN,
                    path=self.img.url
                ),
                'name': self.name_cn,
                'intro': self.intro_cn,
                'detail': self.detail_cn
            }
        else:
            return {
                'img': "{proto}://{domain}{path}".format(
                    proto=config.PROTOCOL,
                    domain=config.DOMAIN,
                    path=self.img.url
                ),
                'name': self.name_en,
                'intro': self.intro_en,
                'detail': self.detail_en
            }

    def save(self, *args, **kwargs):
        nb = Director.objects.count()
        if nb == 0 or (nb == 1 and self.id):
            super(Director, self).save(*args, **kwargs)

    def __str__(self):
        return u'艺术总监'

    class Meta:
        verbose_name = u'艺术总监'
        verbose_name_plural = verbose_name


class InstrumentType(models.Model):
    name_cn = models.CharField(u"乐器名称(中文)", max_length=50, default='')
    name_en = models.CharField(u"乐器名称(英文)", max_length=50, default='')

    def get_abstract(self, lang):
        if lang == 'cn':
            return {'id': self.id, 'name': self.name_cn}
        else:
            return {'id': self.id, 'name': self.name_en}

    def __str__(self):
        return self.name_cn

    class Meta:
        verbose_name = u'乐器种类'
        verbose_name_plural = verbose_name


class Performer(models.Model):
    img = models.ImageField(u"头像", upload_to='image', default=None)
    instrument_type = models.ForeignKey(InstrumentType, verbose_name=u"演奏乐器", default=None)
    name_cn = models.CharField(u"名称(中文)", max_length=20, default='', unique=True)
    detail_cn = models.TextField(u"个人介绍(中文)", default='')
    name_en = models.CharField(u"名称(英文)", max_length=20, default='', unique=True)
    detail_en = models.TextField(u"个人介绍(英文)", default='')

    def get_abstract(self, lang, verbose):
        intro = {
            'id': self.id,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            )
        }
        if lang == 'cn':
            intro['name'] = self.name_cn
            intro['instrument_type'] = self.instrument_type.name_cn
            if verbose == 'detail':
                intro['detail'] = self.detail_cn
        else:
            intro['name'] = self.name_en
            intro['instrument_type'] = self.instrument_type.name_en
            if verbose == 'detail':
                intro['detail'] = self.detail_en
        return intro

    def __str__(self):
        return self.name_cn

    class Meta:
        verbose_name = u'乐团成员'
        verbose_name_plural = verbose_name
