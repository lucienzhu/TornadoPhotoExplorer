__author__ = 'xlzhu'

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import select

class ImageDatabase:
    def init(self):
        #mock-up: initialize and create at each run
        self.engine = create_engine('sqlite:///:memory:', echo=True)

        metadata = MetaData()
        self.images = Table('images', metadata,
            Column('id', Integer, primary_key=True),
            Column('image_url', String),
            Column('thumbnail_url', String),
        )
        metadata.create_all(self.engine)

    def run(self):
        self.connection = self.engine.connect()

    def stop(self):
        pass

    def insert_image_url(self, iu):
        ins = self.images.insert().values(image_url=iu)
        self.connection.execute(ins)

    def insert_all_image_url(self, image_urls):
        ins = self.images.insert()
        for iu in image_urls:
            print "DEBUG:" + iu
            self.connection.execute(ins,image_url=iu)

    def get_all_image_urls(self):
        sel = select([self.images.c.image_url])
        res = self.connection.execute(sel)
        unp = []
        for a in res:
            unp.append({'image_url':a[0]})
        return unp

    def get_all_image_ids_and_urls(self):
        sel = select([self.images.c.id, self.images.c.image_url])
        res = self.connection.execute(sel)
        unp = []
        for a in res:
            unp.append({'id':a[0], 'image_url':a[1]})
        return unp


    def get_image_by_id(self, id):
        sel = select([self.images.c.id, self.images.c.image_url]).where(self.images.c.id == id)
        res = self.connection.execute(sel)
        ires = res.fetchone()
        if ires:
            unp = {'id':ires[self.images.c.id], 'image_url':ires[self.images.c.image_url]}
        else:
            unp = None
        return unp

    def get_3_images_by_id(self, id):
        unps = []
        unps.append(self.get_image_by_id(id-1))
        unps.append(self.get_image_by_id(id))
        unps.append(self.get_image_by_id(id+1))
        return unps

    def update_all_image_urls(self, image_urls):
        durls = self.get_all_image_urls()
        for iu in image_urls:
            matches = [x for x in durls if x == iu]
            if len(matches) <= 0:
                self.insert_image_url(iu)


    def get_all_thumbnail_urls(self):
        sel = select([self.images.c.thumbnail_url])
        res = self.connection.execute(sel)
        unp = []
        for a in res:
            unp.append(a[0])
        return unp
