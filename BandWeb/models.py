# coding=utf-8
import config
import utils
from django.db import models
from storage import ImageStorage
from datetime import datetime
from django.utils.timezone import utc


def default_time_now():
    return datetime.utcnow().replace(tzinfo=utc)


class Banner(models.Model):
    img = models.ImageField(u"轮播图", upload_to='image', default=None, storage=ImageStorage())
    order = models.IntegerField(u"顺序", default=100)
    title_cn = models.CharField(u"主标题(中文)", max_length=100, default='')
    subtitle_cn = models.CharField(u"副标题(中文)", max_length=100, default='')
    title_en = models.CharField(u"主标题(英文)", max_length=100, default='')
    subtitle_en = models.CharField(u"副标题(英文)", max_length=100, default='')

    def get_abstract(self, lang):
        content = {
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url),
            'order': self.order
        }
        if lang == 'cn':
            content['title'] = self.title_cn
            content['subtitle'] = self.subtitle_cn
        else:
            content['title'] = self.title_en
            content['subtitle'] = self.subtitle_en
        return content

    def show_img(self):
        return u'<center><img src="%s" style="height: 100px"/></center>' % self.img.url

    def show_title_cn(self):
        return u'<center><p style="line-height:100px">%s</p></center>' % self.title_cn

    def show_title_en(self):
        return u'<center><p style="line-height:100px">%s</p></center>' % self.title_en

    def show_order(self):
        return u'<center><p style="line-height:100px">%s</p></center>' % self.order

    show_img.allow_tags = True
    show_title_cn.allow_tags = True
    show_title_en.allow_tags = True
    show_order.allow_tags = True
    show_img.short_description = u"<center>%s</center>" % u"轮播图"
    show_order.short_description = u"<center>%s</center>" % u"顺序"
    show_title_cn.short_description = u"<center>%s</center>" % u"主标题(中文)"
    show_title_en.short_description = u"<center>%s</center>" % u"主标题(英文)"

    def __str__(self):
        return self.title_cn

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name


class YueTuanIntro(models.Model):
    content_cn = models.TextField(u"乐团介绍(中文)", default='')
    content_en = models.TextField(u"乐团介绍(英文)", default='')

    def get_abstract(self, lang='cn'):
        if lang == 'cn':
            return {'content': self.content_cn}
        else:
            return {'content': self.content_en}

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
    president_img = models.ImageField(u"团长头像", upload_to='image', default=None, storage=ImageStorage())
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
            'name_cn': self.president_name_cn,
            'name_en': self.president_name_en,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.president_img.url),
            'president_type': int(self.president_type)
        }
        if lang == 'cn':
            intro['intro'] = self.president_intro_cn
            if verbose == 'detail':
                intro['detail'] = self.president_detail_cn
        else:
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
            return {'content': self.address_cn}
        else:
            return {'content': self.address_en}

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
    img = models.ImageField(u"头像", upload_to='image', default=None, storage=ImageStorage())
    name_cn = models.CharField(u"名称(中文)", max_length=20, default='', unique=True)
    intro_cn = models.CharField(u"简介(中文)", max_length=50, default='')
    detail_cn = models.TextField(u"介绍详情(中文)", default='')
    name_en = models.CharField(u"名称(英文)", max_length=20, default='', unique=True)
    intro_en = models.CharField(u"简介(英文)", max_length=50, default='')
    detail_en = models.TextField(u"介绍详情(英文)", default='')

    def get_abstract(self, lang, verbose):
        intro = {
            'id': self.id,
            'name_cn': self.name_cn,
            'name_en': self.name_en,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            ),
        }
        if lang == 'cn':
            intro['intro'] = self.intro_cn
            if verbose == 'detail':
                intro['detail'] = self.detail_cn
            return intro
        else:
            intro['intro'] = self.intro_en
            if verbose == 'detail':
                intro['detail'] = self.detail_en
            return intro

    def __str__(self):
        return self.name_cn

    class Meta:
        verbose_name = u'驻团指挥'
        verbose_name_plural = verbose_name


class Director(models.Model):
    img = models.ImageField(u"头像", upload_to='image', default=None, storage=ImageStorage())
    name_cn = models.CharField(u"名称(中文)", max_length=20, default='')
    intro_cn = models.CharField(u"简介(中文)", max_length=50, default='')
    detail_cn = models.TextField(u"介绍详情(中文)", default='')
    name_en = models.CharField(u"名称(英文)", max_length=20, default='')
    intro_en = models.CharField(u"简介(英文)", max_length=50, default='')
    detail_en = models.TextField(u"介绍详情(英文)", default='')

    def get_abstract(self, lang, verbose):
        intro = {
            'id': self.id,
            'name_cn': self.name_cn,
            'name_en': self.name_en,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            )
        }
        if lang == 'cn':
            intro['intro'] = self.intro_cn
            if verbose == 'detail':
                intro['detail'] = self.detail_cn
            return intro
        else:
            intro['intro'] = self.intro_en
            if verbose == 'detail':
                intro['detail'] = self.detail_en
            return intro

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
    img = models.ImageField(u"头像", upload_to='image', default=None, storage=ImageStorage())
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
            ),
            'name_cn': self.name_cn,
            'name_en': self.name_en
        }
        if lang == 'cn':
            intro['instrument_type'] = self.instrument_type.name_cn
            if verbose == 'detail':
                intro['detail'] = self.detail_cn
        else:
            intro['instrument_type'] = self.instrument_type.name_en
            if verbose == 'detail':
                intro['detail'] = self.detail_en
        return intro

    def __str__(self):
        return self.name_cn

    class Meta:
        verbose_name = u'乐团成员'
        verbose_name_plural = verbose_name


class Musicale(models.Model):
    publish_time = models.DateField(u"发布日期", default=default_time_now)
    title_cn = models.CharField(u"中文标题", max_length=100, unique=True, default='')
    content_cn = models.TextField(u"中文内容", default='')
    title_en = models.CharField(u"英文标题", max_length=100, unique=True, default='')
    content_en = models.TextField(u"英文内容", default='')
    img = models.ImageField(u"图片", upload_to='image', default=None, storage=ImageStorage())

    def get_abstract(self, lang, verbose):
        if lang == 'cn':
            intro = {
                'id': self.id,
                'img': "{proto}://{domain}{path}".format(
                    proto=config.PROTOCOL,
                    domain=config.DOMAIN,
                    path=self.img.url,
                ),
                'title': self.title_cn,
                'date': self.publish_time.strftime('%Y年%m月%d日')
            }
            if verbose == 'detail':
                intro['detail'] = self.content_cn
            return intro
        else:
            intro = {
                'id': self.id,
                'img': "{proto}://{domain}{path}".format(
                    proto=config.PROTOCOL,
                    domain=config.DOMAIN,
                    path=self.img.url,
                ),
                'title': self.title_en,
                'date': self.publish_time.strftime('%Y-%m-%d')
            }
            if verbose == 'detail':
                intro['detail'] = self.content_en
            return intro

    def __str__(self):
        return self.title_cn

    class Meta:
        verbose_name = u'音乐会'
        verbose_name_plural = verbose_name


class MusicFestival(models.Model):
    img = models.ImageField(u"图片", upload_to='image', default=None, storage=ImageStorage())
    publish_time = models.DateField(u"发布日期", default=default_time_now)
    title_cn = models.CharField(u"中文标题", max_length=100, unique=True, default='')
    content_cn = models.TextField(u"中文内容", default='')
    title_en = models.CharField(u"英文标题", max_length=100, unique=True, default='')
    content_en = models.TextField(u"英文内容", default='')

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
            intro['date'] = self.publish_time.strftime('%Y年%m月%d日')
            intro['title'] = self.title_cn
            if verbose == 'abstract':
                intro['abstract'] = utils.clip_n_rows(self.content_cn, lang='cn')
            else:
                intro['detail'] = self.content_cn
        else:
            intro['date'] = self.publish_time.strftime('%Y-%m-%d')
            intro['title'] = self.title_en
            if verbose == 'abstract':
                intro['abstract'] = utils.clip_n_rows(self.content_en, lang='en')
            else:
                intro['detail'] = self.content_en
        return intro

    def __str__(self):
        return self.title_cn

    class Meta:
        verbose_name = u'乐季'
        verbose_name_plural = verbose_name


"""
class BeautyMelodyIntro(models.Model):
    img = models.ImageField(u"天姿国乐展示图", upload_to='image', default=None, storage=ImageStorage())
    detail_cn = models.TextField(u"天姿国乐介绍(中文)", default='')
    detail_en = models.TextField(u"天姿国乐介绍(英文)", default='')

    def get_abstract(self, lang, verbose):
        intro = {
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            )
        }
        if lang == 'cn' and verbose == 'abstract':
            intro['abstract'] = None
        elif lang == 'en' and verbose == 'abstract':
            intro['abstract'] = None
        elif lang == 'cn' and verbose == 'detail':
            intro['detail'] = self.detail_cn
        else:
            intro['detail'] = self.detail_en
        return intro

    def save(self, *args, **kwargs):
        nb = BeautyMelodyIntro.objects.count()
        if nb == 0 or (nb == 1 and self.id):
            super(BeautyMelodyIntro, self).save(*args, **kwargs)

    def __str__(self):
        return u'天姿国乐介绍'

    class Meta:
        verbose_name = u'天姿国乐介绍'
        verbose_name_plural = verbose_name
"""


class BeautyMelodyNews(models.Model):
    img = models.ImageField(u"缩略图", upload_to='image', default='', storage=ImageStorage())
    publish_time = models.DateField(u"发布日期", default=default_time_now)
    title_cn = models.CharField(u"文章标题(中文)", max_length=50, default='')
    detail_cn = models.TextField(u"文章内容(中文)", default='')
    title_en = models.CharField(u"文章标题(英文)", max_length=50, default='')
    detail_en = models.TextField(u"文章内容(英文)", default='')

    def get_abstract(self, lang, verbose):
        content = {
            'id': self.id,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            )
        }
        if lang == 'cn':
            content['title'] = self.title_cn
            content['date'] = self.publish_time.strftime('%Y年%m月%d日')
            if verbose == 'abstract':
                content['abstract'] = utils.clip_text(self.detail_cn, keep_n=50, lang='cn')
            else:
                content['detail'] = self.detail_cn
        else:
            content['title'] = self.title_en
            content['date'] = self.publish_time.strftime('%Y-%m-%d')
            if verbose == 'abstract':
                content['abstract'] = utils.clip_text(self.detail_en, keep_n=100, lang='en')
            else:
                content['detail'] = self.detail_en
        return content

    def __str__(self):
        return self.title_cn

    class Meta:
        verbose_name = u'国乐新闻'
        verbose_name_plural = verbose_name

"""
class OperaIntro(models.Model):
    img = models.ImageField(u"歌剧院展示图", upload_to='image', default=None, storage=ImageStorage())
    detail_cn = models.TextField(u"歌剧院介绍(中文)", default='')
    detail_en = models.TextField(u"歌剧院介绍(英文)", default='')

    def get_abstract(self, lang, verbose):
        intro = {
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            )
        }
        if lang == 'cn' and verbose == 'abstract':
            intro['abstract'] = None
        elif lang == 'en' and verbose == 'abstract':
            intro['abstract'] = None
        elif lang == 'cn' and verbose == 'detail':
            intro['detail'] = self.detail_cn
        else:
            intro['detail'] = self.detail_en
        return intro

    def save(self, *args, **kwargs):
        nb = OperaIntro.objects.count()
        if nb == 0 or (nb == 1 and self.id):
            super(OperaIntro, self).save(*args, **kwargs)

    def __str__(self):
        return u'歌剧院介绍'

    class Meta:
        verbose_name = u'歌剧院介绍'
        verbose_name_plural = verbose_name
"""


class OperaNews(models.Model):
    img = models.ImageField(u"缩略图", upload_to='image', default='', storage=ImageStorage())
    publish_time = models.DateField(u"发布日期", default=default_time_now)
    title_cn = models.CharField(u"文章标题(中文)", max_length=50, default='')
    detail_cn = models.TextField(u"文章内容(中文)", default='')
    title_en = models.CharField(u"文章标题(英文)", max_length=50, default='')
    detail_en = models.TextField(u"文章内容(英文)", default='')

    def get_abstract(self, lang, verbose):
        content = {
            'id': self.id,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            )
        }
        if lang == 'cn':
            content['title'] = self.title_cn
            content['date'] = self.publish_time.strftime('%Y年%m月%d日')
            if verbose == 'abstract':
                content['abstract'] = utils.clip_text(self.detail_cn, keep_n=50, lang='cn')
            else:
                content['detail'] = self.detail_cn
        else:
            content['title'] = self.title_en
            content['date'] = self.publish_time.strftime('%Y-%m-%d')
            if verbose == 'abstract':
                content['abstract'] = utils.clip_text(self.detail_en, keep_n=100, lang='en')
            else:
                content['detail'] = self.detail_en
        return content

    def __str__(self):
        return self.title_cn

    class Meta:
        verbose_name = u'歌剧院新闻'
        verbose_name_plural = verbose_name


class BusinessDynamics(models.Model):
    img = models.ImageField(u"缩略图", upload_to='image', default='', storage=ImageStorage())
    publish_time = models.DateField(u"发布日期", default=default_time_now)
    title_cn = models.CharField(u"文章标题(中文)", max_length=50, default='')
    detail_cn = models.TextField(u"文章内容(中文)", default='')
    title_en = models.CharField(u"文章标题(英文)", max_length=50, default='')
    detail_en = models.TextField(u"文章内容(英文)", default='')

    def get_abstract(self, lang, verbose):
        content = {
            'id': self.id,
            'img': "{proto}://{domain}{path}".format(
                proto=config.PROTOCOL,
                domain=config.DOMAIN,
                path=self.img.url
            )
        }
        if lang == 'cn':
            content['title'] = self.title_cn
            content['date'] = self.publish_time.strftime('%Y年%m月%d日')
            if verbose == 'abstract':
                content['abstract'] = utils.clip_text(self.detail_cn, keep_n=50, lang='cn')
            else:
                content['detail'] = self.detail_cn
        else:
            content['title'] = self.title_en
            content['date'] = self.publish_time.strftime('%Y-%m-%d')
            if verbose == 'abstract':
                content['abstract'] = utils.clip_text(self.detail_en, keep_n=100, lang='en')
            else:
                content['detail'] = self.detail_en
        return content

    def __str__(self):
        return self.title_cn

    class Meta:
        verbose_name = u'事业动态'
        verbose_name_plural = verbose_name
