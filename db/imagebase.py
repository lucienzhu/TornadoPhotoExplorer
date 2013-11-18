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
        )
        metadata.create_all(self.engine)

    def run(self):
        self.connection = self.engine.connect()

    def stop(self):
        pass

    def insert_image_url(self, iu):
        ins = self.images.insert().values(image_url=iu)
        self.connection.excute(ins)

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
            unp.append(a[0])
        return unp
