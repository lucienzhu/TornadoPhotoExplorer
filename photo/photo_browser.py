__author__ = 'xlzhu'

import glob
import globals
import image_processer as imp
from db import image_base as ib

class PhotoBrowser:
    def __init__(self, image_db=None):
        self.image_db = image_db;

    def get_all_photo_urls(self):
        photo_urls = self.image_db.get_all_image_urls()
        return self.photo_urls

    def get_all_photo_ids_and_urls(self):
        photo_ids_urls = self.image_db.get_all_image_ids_urls()
        return self.photo_ids_urls

    def get_all_thumbnail_urls(self):
        pass

    def save_all_photo_thumbnails(self):
        pass