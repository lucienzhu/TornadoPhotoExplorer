#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

from tornado.options import define, options

from photo import photo
from db import imagebase
from log import log

define('port', default=1013, help='run on the given port', type=int)



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r'/DATA/(.*)', tornado.web.StaticFileHandler, {'path': 'DATA/'}),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # database: define a global database
        self.db = imagebase.ImageDatabase()
        self.db.init()
        self.db.run()

        self.logger = log.Logger()

        # scan folder
        self.ib = photo.PhotoBrowser()

        # save all thumbnails
        self.ib.save_all_photo_thumbnails()
        image_urls = self.ib.get_all_thumbnail_urls()
        self.db.insert_all_image_url(image_urls=image_urls)

        self.logger.log("Initialization Done!!!")


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class HomeHandler(BaseHandler):
    def get(self):
        img_urls = self.db.get_all_image_urls()
        self.render("index.html", image_urls = img_urls)

        self.logger = log.Logger()
        self.logger.log("Home.")


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
