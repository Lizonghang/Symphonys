# coding=utf-8
from Symphonys import settings
import os
import re
import time
import config
import random


class UploadMediaManager:
    def __init__(self):
        self.BASE_DIR = os.path.join(settings.BASE_DIR, 'assets', 'media')

    def save(self, media_type, media_data):
        filename = 'fulltext_' + time.strftime('%Y%m%d%H%M%S') + str(random.randint(100, 999)) + '.jpg'
        store_path = os.path.join(self.BASE_DIR, media_type, filename)
        with open(store_path, 'wb') as fp:
            fp.write(media_data.read())
        return '{protocol}://{domain}/assets/media/{type}/{filename}'.format(
            protocol=config.PROTOCOL,
            domain=config.DOMAIN,
            type=media_type,
            filename=filename
        )


def clip_text(raw_text, keep_n=50, lang='cn'):
    raw_intro = re.sub(u'&nbsp;', '', raw_text)
    raw_intro = re.sub(u'&emsp;', '', raw_intro)
    raw_intro = re.sub(u'<.*?>', '', raw_intro)
    raw_intro = re.sub(u'[\r\n\t]', '', raw_intro)
    if len(raw_intro) < keep_n:
        return raw_intro
    if lang == 'en':
        while raw_intro[keep_n].isalpha():
            keep_n += 1
    return raw_intro[:keep_n] + '...'
