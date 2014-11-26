import base_worker
#from photo import image_processer as imp

__author__ = 'xlzhu'

class ThumbnailManager(base_worker.BaseWorker):
    def __init__(self, image_db=None):
        base_worker.BaseWorker.__init__(self, image_db)
        self.name = self.__class__.__name__


    def run_once(self):
        self.save_all_photo_thumbnails();


    def save_all_photo_thumbnails(self):
        pass