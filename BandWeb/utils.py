# coding=utf-8
from Symphonys import settings
from datetime import datetime
import os
import config


class UploadMediaManager:
    def __init__(self):
        self.BASE_DIR = os.path.join(settings.BASE_DIR, 'assets', 'media')

    def save(self, media_type, media_data):
        filename = '{0}.jpg'.format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
        store_path = os.path.join(self.BASE_DIR, media_type, filename)
        with open(store_path, 'wb') as fp:
            fp.write(media_data.read())
        return '{protocol}://{domain}/assets/media/{type}/{filename}'.format(
            protocol=config.PROTOCOL,
            domain=config.DOMAIN,
            type=media_type,
            filename=filename
        )
