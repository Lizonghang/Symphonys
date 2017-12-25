# encoding: utf-8
from xadmin.views import CommAdminView, BaseAdminView
from xadmin.layout import Main, Fieldset
from models import *
import xadmin


class GlobalSetting(object):
    """ Bind to CommAdminView """
    site_title = u"四川交响乐团|后台管理系统"
    site_footer = u"四川交响乐团|四川大学"
    menu_style = 'accordion'
    apps_label_title = {
        'auth': u'管理员账户',
        'symphonys': u'应用模型',
    }

    def get_nav_menu(self):
        return [
            {
                'menus': [
                    {
                        'url': u'/backend/xadmin/auth/user/',
                        'icon': 'fa fa-user',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'账户'
                    }
                ],
                'first_icon': 'fa fa-user',
                'first_url': u'/backend/xadmin/auth/user/',
                'title': u'账户管理'
            },
            {
                'menus': [
                    {
                        'url': u'/backend/xadmin/BandWeb/banner/',
                        'icon': 'fa fa-music',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'轮播图'
                    }
                ],
                'first_icon': 'fa fa-music',
                'first_url': u'/backend/xadmin/BandWeb/banner/',
                'title': u'首页'
            },
            {
                'menus': [
                    {
                        'url': u'/backend/xadmin/BandWeb/yuetuanintro/',
                        'icon': 'fa fa-music',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'乐团介绍'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/yuetuanleader/',
                        'icon': 'fa fa-music',
                        'order': 2,
                        'perm': 'auth.view_user',
                        'title': u'乐团团长'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/presidentaddress/',
                        'icon': 'fa fa-music',
                        'order': 3,
                        'perm': 'auth.view_user',
                        'title': u'团长致辞'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/conductor/',
                        'icon': 'fa fa-music',
                        'order': 4,
                        'perm': 'auth.view_user',
                        'title': u'驻团指挥'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/director/',
                        'icon': 'fa fa-music',
                        'order': 5,
                        'perm': 'auth.view_user',
                        'title': u'艺术总监'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/instrumenttype/',
                        'icon': 'fa fa-music',
                        'order': 6,
                        'perm': 'auth.view_user',
                        'title': u'乐器种类'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/performer/',
                        'icon': 'fa fa-music',
                        'order': 7,
                        'perm': 'auth.view_user',
                        'title': u'乐团成员'
                    }
                ],
                'first_icon': 'fa fa-music',
                'first_url': u'/backend/xadmin/BandWeb/yuetuanintro/',
                'title': u'乐团介绍'
            },
            {
                'menus': [
                    {
                        'url': u'/backend/xadmin/BandWeb/musicale/',
                        'icon': 'fa fa-music',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'音乐会'
                    }
                ],
                'first_icon': 'fa fa-music',
                'first_url': u'/backend/xadmin/BandWeb/musicale/',
                'title': u'音乐会'
            },
            {
                'menus': [
                    {
                        'url': u'/backend/xadmin/BandWeb/beautymelodyintro/',
                        'icon': 'fa fa-music',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'介绍'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/beautymelodynews/',
                        'icon': 'fa fa-music',
                        'order': 2,
                        'perm': 'auth.view_user',
                        'title': u'新闻'
                    }
                ],
                'first_icon': 'fa fa-music',
                'first_url': u'/backend/xadmin/BandWeb/beautymelodyintro/',
                'title': u'天姿国乐'
            },
            {
                'menus': [
                    {
                        'url': u'/backend/xadmin/BandWeb/operaintro/',
                        'icon': 'fa fa-music',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'介绍'
                    },
                    {
                        'url': u'/backend/xadmin/BandWeb/operanews/',
                        'icon': 'fa fa-music',
                        'order': 2,
                        'perm': 'auth.view_user',
                        'title': u'新闻'
                    }
                ],
                'first_icon': 'fa fa-music',
                'first_url': u'/backend/xadmin/BandWeb/operaintro/',
                'title': u'歌剧院'
            },
            {
                'menus': [
                    {
                        'url': u'/backend/xadmin/BandWeb/businessdynamics/',
                        'icon': 'fa fa-music',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'事业动态'
                    }
                ],
                'first_icon': 'fa fa-music',
                'first_url': u'/backend/xadmin/BandWeb/businessdynamics/',
                'title': u'事业动态'
            }
        ]


class BaseSetting(object):
    """ Bind to BaseAdminView """
    enable_themes = True
    use_bootswatch = True


class RichTextAdmin(object):
    def get_media(self):
        """
        :return: media
        :description: 为弥补xadmin中不支持class Media指定js文件插入的缺陷,
                      此处复写父类get_media方法,将xadmin默认引入文件与自定义
                      js文件(通过media.add_js添加)一起引入管理后台页面.
        """

        media = super(RichTextAdmin, self).get_media()
        media.add_js((
            'kindeditor/kindeditor-all.js',
            'kindeditor/lang/zh-CN.js',
            'kindeditor/config.js',
        ))
        return media


class MusicaleAdmin(RichTextAdmin):
    list_display = ('title_cn', 'title_en', 'update')
    list_filter = ('title_cn', 'title_en', 'update')
    search_fields = ('title_cn', 'title_en', 'update')
    list_editable = ('title_cn', 'title_en')
    form_layout = (
        Main(
            Fieldset('中文信息', 'title_cn', 'update', 'content_cn'),
            Fieldset('英文信息', 'title_en', 'update', 'content_en'),
        ),
    )


class BannerAdmin(object):
    list_display = ('title_cn', 'title_en', 'order')
    form_layout = (
        Main(
            Fieldset('图片与顺序', 'img', 'order'),
            Fieldset('中文题目', 'title_cn', 'subtitle_cn'),
            Fieldset('英文题目', 'title_en', 'subtitle_en')
        )
    )


class YueTuanIntroAdmin(RichTextAdmin):
    form_layout = (
        Main(
            Fieldset('中文介绍', 'content_cn'),
            Fieldset('英文介绍', 'content_en'),
        ),
    )


class YueTuanLeaderAdmin(object):
    list_display = ('president_name_cn', 'president_name_en', 'president_type')
    form_layout = (
        Main(
            Fieldset('基本信息', 'president_img', 'president_type'),
            Fieldset('中文信息', 'president_name_cn', 'president_intro_cn', 'president_detail_cn'),
            Fieldset('英文信息', 'president_name_en', 'president_intro_en', 'president_detail_en')
        ),
    )


class PresidentAddressAdmin(RichTextAdmin):
    form_layout = (
        Main(
            Fieldset('中文致辞', 'address_cn'),
            Fieldset('英文致辞', 'address_en')
        ),
    )


class ConductorAdmin(RichTextAdmin):
    list_display = ('name_cn', 'name_en', 'intro_cn', 'intro_en')
    form_layout = (
        Main(
            Fieldset('头像', 'img'),
            Fieldset('中文信息', 'name_cn', 'intro_cn', 'detail_cn'),
            Fieldset('英文信息', 'name_en', 'intro_en', 'detail_en')
        )
    )


class DirectorAdmin(RichTextAdmin):
    list_display = ('name_cn', 'name_en', 'intro_cn', 'intro_en')
    form_layout = (
        Main(
            Fieldset('头像', 'img'),
            Fieldset('中文信息', 'name_cn', 'intro_cn', 'detail_cn'),
            Fieldset('英文信息', 'name_en', 'intro_en', 'detail_en')
        )
    )


class PerformerAdmin(RichTextAdmin):
    list_display = ('name_cn', 'name_en', 'instrument_type__name_cn')
    list_filter = ('instrument_type__name_cn',)
    form_layout = (
        Main(
            Fieldset('头像', 'img'),
            Fieldset('中文信息', 'name_cn', 'detail_cn', 'instrument_type'),
            Fieldset('英文信息', 'name_en', 'detail_en')
        )
    )


class BeautyMelodyIntroAdmin(RichTextAdmin):
    form_layout = (
        Main(
            Fieldset('展示图', 'img'),
            Fieldset('中文介绍', 'detail_cn'),
            Fieldset('英文介绍', 'detail_en')
        )
    )


class BeautyMelodyNewsAdmin(RichTextAdmin):
    list_display = ('title_cn', 'title_en', 'publish_time')
    form_layout = (
        Main(
            Fieldset('缩略图', 'img'),
            Fieldset('中文信息', 'title_cn', 'detail_cn'),
            Fieldset('英文信息', 'title_en', 'detail_en')
        )
    )


class OperaIntroAdmin(RichTextAdmin):
    form_layout = (
        Main(
            Fieldset('展示图', 'img'),
            Fieldset('中文介绍', 'detail_cn'),
            Fieldset('英文介绍', 'detail_en')
        )
    )


class OperaNewsAdmin(RichTextAdmin):
    list_display = ('title_cn', 'title_en', 'publish_time')
    form_layout = (
        Main(
            Fieldset('缩略图', 'img'),
            Fieldset('中文信息', 'title_cn', 'detail_cn'),
            Fieldset('英文信息', 'title_en', 'detail_en')
        )
    )


class BusinessDynamicsAdmin(RichTextAdmin):
    list_display = ('title_cn', 'title_en', 'publish_time')
    form_layout = (
        Main(
            Fieldset('缩略图', 'img'),
            Fieldset('中文信息', 'title_cn', 'detail_cn'),
            Fieldset('英文信息', 'title_en', 'detail_en')
        )
    )

xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(Musicale, MusicaleAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(YueTuanIntro, YueTuanIntroAdmin)
xadmin.site.register(YueTuanLeader, YueTuanLeaderAdmin)
xadmin.site.register(PresidentAddress, PresidentAddressAdmin)
xadmin.site.register(Conductor, ConductorAdmin)
xadmin.site.register(Director, DirectorAdmin)
xadmin.site.register(InstrumentType)
xadmin.site.register(Performer, PerformerAdmin)
xadmin.site.register(BeautyMelodyIntro, BeautyMelodyIntroAdmin)
xadmin.site.register(BeautyMelodyNews, BeautyMelodyNewsAdmin)
xadmin.site.register(OperaIntro, OperaIntroAdmin)
xadmin.site.register(OperaNews, OperaNewsAdmin)
xadmin.site.register(BusinessDynamics, BusinessDynamicsAdmin)
