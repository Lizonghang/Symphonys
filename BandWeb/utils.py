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


def clip_n_rows(raw_html, lang='cn', row_max=4, width_max=18):
    raw_text = re.sub(u'<.*?>', '', raw_html)
    raw_text = re.sub(u'[\r\t]', '', raw_text)
    raw_text = re.sub(u'[\n]', ' ', raw_text)
    raw_text = '\n'.join(raw_text.strip().split())
    row = 1
    word = 0
    i = 0
    while True:
        if row == 5:
            break
        if u'\u4e00' <= raw_text[i] <= u'\u9fa5':
            word += 1
        if word == width_max:
            word = 0
            row += 1
        if raw_text[i] == '\n':
            word = 0
            row += 1
        i += 1
    return raw_text[:i-2] + '...'
