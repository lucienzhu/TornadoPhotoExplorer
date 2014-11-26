import tornado.httpserver
from log import log

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class HomeHandler(BaseHandler):
    def get(self):
        img_ids_urls = self.db.get_all_image_ids_and_urls()
        self.render("index.html", image_ids_urls = img_ids_urls)

        self.logger = log.Logger()
        self.logger.log("Home.")


class PhotoHandler(BaseHandler):
    def get(self, slug):
        img = self.db.get_3_images_by_id(int(float(slug)))
        self.render("photo.html", images = img)

        self.logger = log.Logger()
        self.logger.log("Query image %id" % id)