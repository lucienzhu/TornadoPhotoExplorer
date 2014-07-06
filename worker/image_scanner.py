'''
ImageScaner.py: scan the folder and update the database
'''

import base_worker
import glob
import globals
from db import image_base as ib

__author__ = 'xlzhu'

class ImageScanner(base_worker.BaseWorker):
    def __init__(self, image_db=None):
        base_worker.BaseWorker.__init__(self, image_db)
        self.name = self.__class__.__name__

    def run_once(self):
        self.update_all_photo_urls()
        #self.update_all_thumbnail_urls()

    def update_all_photo_urls(self):
        photo_urls = glob.glob(globals.IMAGE_FOLDER + '*.JPG')

        self.image_db.update_all_image_urls(photo_urls)

    #def update_all_thumbnail_urls(self):
    #    tn_urls = glob.glob(globals.THUMBNAIL_FOLDER + '*.JPG')
    #    db = ib.ImageDatabase()
    #    db.update_all_thumbnail_urls(tn_urls);

