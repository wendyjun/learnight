# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class DcnPipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect(
                host='localhost',
                port = 3306,
                user='root',
                passwd=' ',
                db ='mysql',
                charset='utf8'
                )
    def process_item(self, item, spider):
        cur=self.conn.cursor()
        sql="""INSERT INTO dcn1(game_name,game_type_name,game_time,game_content) VALUES ('%s','%s','%s','%s')""" % (
                           item['game_name'].encode('utf8'),
                           item['game_type_name'].encode('utf8'),
                           item['game_time'].encode('utf8'),
                           item['game_content'].encode('utf8')
                           )
        cur.execute(sql)
        self.conn.commit()
        cur.close()

        return item
