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
                        'icon': 'fafa-user',
                        'order': 1,
                        'perm': 'auth.view_user',
                        'title': u'账户'
                    }
                ],
                'first_icon': 'fafa-user',
                'first_url': u'/backend/xadmin/auth/user/',
                'title': u'管理员账户'
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


xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(BaseAdminView, BaseSetting)
