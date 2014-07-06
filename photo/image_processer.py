__author__ = 'xlzhu'

from skimage import io
from skimage import transform

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