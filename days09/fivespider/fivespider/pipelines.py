# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import pymysql.cursors

pymysql.install_as_MySQLdb()
from scrapy import log



class CleanPipeline(object):
    def __init__(self):
        self.has = set()

    def process_item(self, item, spider):
        if item.keys() >= 5:
            if item in self.has:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.has.add(item)
                return item


class MySQLPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def form_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self.__do__insert, item, spider)
        d.addBoth(lambda _: item)
        return d

    def __do__insert(self, conn, item, spider):
        try:
            conn.execute = "insert into 58pbdndb(title, area, price, quality, times) values('%s', '%s', '%s','%s','%s')" % \
                     (item['title'], item['area'], item['price'],item['quality'],item['times'])
        except pymysql.Error, e:
            spider.log("Mysql Error %d: %s" % (e.args[0], e.args[1]), level=log.DEBUG)


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # 引入数据库连接模块：引入pymsyql模块，主要用于替代sqlalchemy底层的mysqldb模块来连接数据库
# import pymysql
#
# pymysql.install_as_MySQLdb()
#
#
# class ZlspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#
# class ZhilianPipeline(object):
#     '''
#     定义智联招聘程序处理管道类型，主要进行采集数据的验证和数据存储工作
#     '''
#
#     def __init__(self):
#         # 创建数据库引擎并创建连接会话对象
#         engine = create_engine("mysql://root:123456@localhost:3306/py1709_spider?charset=utf8")
#         # 创建会话
#         Session = sessionmaker(bind=engine)
#         self.session = Session()
#
#     def close_spider(self, spider):
#         # 该函数主要用于进行资源回收操作
#         self.session.commit()
#         self.session.close()
#
#     def process_item(self, item, spider):
#         '''
#         管道核心函数，进行数据验证和存储要操作的地方
#         :param item:
#         :param spider:
#         :return:
#         '''
#         # 构建sql语句
#         zl_sql = "insert into 58pbdndb(title, area, price, quality, times) values('%s', '%s', '%s','%s','%s')" % \
#                      (item['title'], item['area'], item['price'],item['quality'],item['times'])
#
#         # 执行sql语句
#         self.session.execute(zl_sql)