# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 需要模块
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# # 数据库连接模块，替代底层mysqldb
# import pymysql
#
# pymysql.install_as_MySQLdb()
#
#
# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#
# class ZhilianPipeline(object):
#     """
#     定义智联招聘程序处理管道类型，主要进行采集数据的验证和数据存储工作
#     """
#
#     def __init__(self):
#         # 创建数据库引擎并创建连接会话对象
#         engine = create_engine("mysql://root:123456@localhost/py1709_spider?charset=utf8")
#         # 创建会话
#         Session = sessionmaker(bind=engine)
#         self.session = Session()

# def open_spider(self,spider):
#     pass
#
#
# def close_spider(self,spider):
#     #该函数主要用于进行资源回收操作
#     self.session.commit()
#     self.session.close()
#
# def process_item(self,item,spider):
#
#     # 该函数会在爬虫采集并封装好ITEM对象时自动调用
#     # 函数中针对item数据进行验证和存储
#
#     sql = "insert into jobs(job, company, salary) values('%s', '%s', '%s')" \
#           % (item['job'], item['company'], item['salary'])
#     # 执行sql语句
#     self.session.execute(sql)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 引入数据库连接模块：引入pymsyql模块，主要用于替代sqlalchemy底层的mysqldb模块来连接数据库
import pymysql

pymysql.install_as_MySQLdb()


class ZlspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ZhilianPipeline(object):
    '''
    定义智联招聘程序处理管道类型，主要进行采集数据的验证和数据存储工作
    '''

    def __init__(self):
        # 创建数据库引擎并创建连接会话对象
        engine = create_engine("mysql://root:123456@localhost:3306/py1709_spider?charset=utf8")
        # 创建会话
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        # 该函数主要用于进行资源回收操作
        self.session.commit()
        self.session.close()

    def process_item(self, item, spider):
        '''
        管道核心函数，进行数据验证和存储要操作的地方
        :param item:
        :param spider:
        :return:
        '''
        # 构建sql语句
        zl_sql = "insert into jobs(job, company, salary) values('%s', '%s', '%s')" % \
                 (item['job'], item['company'], item['salary'])

        # 执行sql语句
        self.session.execute(zl_sql)
