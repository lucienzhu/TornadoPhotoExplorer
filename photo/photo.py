__author__ = 'xlzhu'

import glob

from skimage import io
from skimage import transform

ROOT_FOLDER = 'DATA/'
IMAGE_FOLDER = ROOT_FOLDER + 'images/'
THUMBNAIL_FOLDER = ROOT_FOLDER + 'thumbnails/'

class PhotoBrowser:
    def get_all_photo_urls(self):
        self.photo_urls = glob.glob(IMAGE_FOLDER + '*.JPG')
        print self.photo_urls
        return self.photo_urls

    def get_all_thumbnail_urls(self):
        self.photo_urls = glob.glob(THUMBNAIL_FOLDER + '*.JPG')
        print self.photo_urls
        return self.photo_urls

    def save_all_photo_thumbnails(self):
        ip = ImageProcessor()
        urls = self.get_all_photo_urls()

        for url in urls:
            im = ip.read_image(url)
            ims = ip.get_square_image(im)
            tb = ip.get_thumbnail(ims, 128, 128)
            ip.save_image(tb, THUMBNAIL_FOLDER + url.split('/')[-1])

class ImageProcessor:
    def read_image(self, local_url):
        im = io.imread(local_url)
        return im

    def get_square_image(self, im):
        ims = im
        return ims

    def get_thumbnail(self, im, size_x, size_y):
        ims = self.get_square_image(im)
        tb = transform.resize(ims, (size_x, size_y))
        return tb

    def save_image(self, im, local_url):
        io.imsave(local_url, im)
