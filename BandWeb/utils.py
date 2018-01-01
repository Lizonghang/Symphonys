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


def clip_n_rows(raw_html, lang='cn', row_max=4):
    if lang == 'cn':
        raw_text = re.sub(u'<.*?>', '', raw_html)
        raw_text = re.sub(u'[\r\t]', '', raw_text)
        raw_text = re.sub(u'[\n]', ' ', raw_text)
        raw_text = '\n'.join(raw_text.strip().split())
        if 'a' <= raw_text[0] <= 'z' or 'A' <= raw_text[0] <= 'Z':
            return 'Invalid Language'
        row = 1
        word = 0
        i = 0
        terminal = False
        while True:
            if row == row_max + 1:
                break
            try:
                if u'\u4e00' <= raw_text[i] <= u'\u9fa5':
                    word += 1
            except IndexError:
                terminal = True
                break
            if word == 18 or raw_text[i] == '\n':
                word = 0
                row += 1
            i += 1
        if terminal:
            return raw_text
        else:
            return raw_text[:i-3] + '...'
    else:
        raw_text = re.sub(u'<.*?>', '', raw_html)
        raw_text = re.sub(u'[\r\t]', '', raw_text)
        if u'\u4e00' <= raw_text[0] <= u'\u9fa5':
            return 'Invalid Language'
        row = 1
        char = 0
        i = 0
        terminal = False
        while True:
            if row == row_max + 1:
                break
            try:
                if 'a' <= raw_text[i] <= 'z' or 'A' <= raw_text[i] <= 'Z':
                    char += 1
            except IndexError:
                terminal = True
                break
            if char == 36 or raw_text[i] == '\n':
                char = 0
                row += 1
            i += 1
        if terminal:
            return raw_text
        else:
            return raw_text[:i-3] + '...'
