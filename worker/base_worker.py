__author__ = 'xlzhu'

class BaseWorker:
    def __init__(self, image_db=None):
        self.name = 'BaseWorker'
        self.image_db = image_db

    def run_once(self):
        pass