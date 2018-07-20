#!/usr/bin/python3
# -*- coding:UTF-8 -*-
#@author:HYX
#@mailbox:1814232115@qq.com

from bs4 import BeautifulSoup
import requests
import pymysql
import os


# 打开数据库连接
db = pymysql.connect("localhost","username","password","DATABASE_name")
#显然，"username","password","DATABASE_name"乃至下面的table_name等都应该私人订制
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS SINA_LINKS")

# 使用预处理语句创建表
sql_str = """	CREATE TABLE SINA_LINKS (
		LINK_ID  INT UNSIGNED AUTO_INCREMENT,
		LINK_TEXT  CHAR(40),
		LINK_URL CHAR(255),
		LINK_NEWS_CONTENT VARCHAR(10000),
		PRIMARY KEY(LINK_ID)
		)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;	"""
 
cursor.execute(sql_str)
# 提交到数据库执行
db.commit()
# 关闭数据库连接
db.close()


#插入操作函数
def insert_into(LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT):
	# 打开数据库连接
	db = pymysql.connect("localhost","hyx","1154007hyx","LINKS")

	# 使用cursor()方法获取操作游标
	cursor = db.cursor()

	# SQL 插入语句 # SQL 插入语句
	sql_str = ("INSERT INTO SINA_LINKS(LINK_ID,LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT)" + "VALUES(NULL,'%s','%s','%s')" % (LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT))
	#之前把LINK写成LINT了，现在已经改回来了................................
	try:
	   # 执行sql语句
	   cursor.execute(sql_str)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # 如果发生错误则回滚
	   print("----Failed!!!")

	   #出错暂停便于调试
	   os.system("pause");
	   db.rollback()

	# 关闭数据库连接
	db.close()
	#print("------------------FINISH LINE---------------------")



server = 'http://news.sina.com.cn/'
target = 'http://news.sina.com.cn/'
req = requests.get(url = target)
req.encoding = 'utf-8'
html = req.text
li_list_bf = BeautifulSoup(html,"html.parser")
li_list = li_list_bf.find_all('li')
alink_bf = BeautifulSoup(str(li_list),"html.parser")
alink = alink_bf.find_all('a')


# 打开数据库连接
db = pymysql.connect("localhost","hyx","1154007hyx","LINKS")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
sql = ("DELETE FROM SINA_LINKS;")
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
# 关闭数据库连接
db.close()

for each in alink:
	if len(each.text) > 0:
		LINK_TEXT = each.text
		LINK_URL = each.get('href')
		print("LINK_TEXT = %s" % (LINK_TEXT))
		print("LINK_URL = %s" % (LINK_URL))
		if len(LINK_TEXT) > 5:
			#只读取超过5个字的链接的详细内容
			target = LINK_URL
			link_req = requests.get(url = target)
			gbk_link = 'http://slide.news.sina.com.cn'
			if gbk_link in target:
				#GBK编码和utf-8编码适配
				link_req.encoding = 'gbk'
			else:
				link_req.encoding = 'utf-8'

			link_html = link_req.text
			article_bf = BeautifulSoup(link_html,"html.parser")
			article = article_bf.find_all('div', class_ = 'article')
			pp_bf = BeautifulSoup(str(article),"html.parser")
			pp = pp_bf.find_all('p')

			begin_mark = 0
			con_mark=0
			for each in pp:
				if begin_mark == 0:
					print("")
					print("-----------------------------------本篇报道开始-----------------------------------")
					begin_mark = 1

				p=each.text
				print(p)
				if con_mark==0:
					LINK_NEWS_CONTENT=p
					con_mark=1
				else:
					LINK_NEWS_CONTENT = LINK_NEWS_CONTENT+p


			if begin_mark==1:
				print("-----------------------------------本篇报道结束-----------------------------------")
				print("")
		else:
			LINK_NEWS_CONTENT = None
		#插入表格
		insert_into(LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT)
		#使用完毕立即清空
		LINK_NEWS_CONTENT = None
		#输出LINK_TEXT和LINK_URL后一定要有换行
		print("")
print("......完成")
