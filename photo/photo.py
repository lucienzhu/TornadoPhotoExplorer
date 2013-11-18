__author__ = 'xlzhu'

import glob

ROOT_FOLDER = 'DATA/'
IMAGE_FOLDER = ROOT_FOLDER + 'images/'

class PhotoBrowser:
    def get_all_photo_urls(self):
        self.photo_urls = glob.glob(IMAGE_FOLDER + '*.JPG')
        print self.photo_urls
        return self.photo_urls
