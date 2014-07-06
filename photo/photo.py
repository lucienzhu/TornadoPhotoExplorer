__author__ = 'xlzhu'

import datetime as dt
import globals


class BasePhoto:
    '''Photo relate to I/O'''

    def __init__(self):
        self.filename_ = ''
        self.folder_ = ''
        self.create_time_ = dt.datetime.now()
        self.modify_time_ = dt.datetime.now()


class Photo(BasePhoto):
    '''Normal photo'''

    def __init__(self):
        self.super.__init__()
        self.image_ = None;  # data as skimage, just a NumPy array.
        self.caption_ = self.filename_
