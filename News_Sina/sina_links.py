#!/usr/bin/python3
# -*- coding:UTF-8 -*-
#@author:HYX
#@mailbox:1814232115@qq.com

from bs4 import BeautifulSoup
import requests
import pymysql
import os


# �����ݿ�����
db = pymysql.connect("localhost","username","password","DATABASE_name")
#��Ȼ��"username","password","DATABASE_name"���������table_name�ȶ�Ӧ��˽�˶���
# ʹ�� cursor() ��������һ���α���� cursor
cursor = db.cursor()

# ʹ�� execute() ����ִ�� SQL������������ɾ��
cursor.execute("DROP TABLE IF EXISTS SINA_LINKS")

# ʹ��Ԥ������䴴����
sql_str = """	CREATE TABLE SINA_LINKS (
		LINK_ID  INT UNSIGNED AUTO_INCREMENT,
		LINK_TEXT  CHAR(40),
		LINK_URL CHAR(255),
		LINK_NEWS_CONTENT VARCHAR(10000),
		PRIMARY KEY(LINK_ID)
		)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;	"""
 
cursor.execute(sql_str)
# �ύ�����ݿ�ִ��
db.commit()
# �ر����ݿ�����
db.close()


#�����������
def insert_into(LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT):
	# �����ݿ�����
	db = pymysql.connect("localhost","hyx","1154007hyx","LINKS")

	# ʹ��cursor()������ȡ�����α�
	cursor = db.cursor()

	# SQL ������� # SQL �������
	sql_str = ("INSERT INTO SINA_LINKS(LINK_ID,LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT)" + "VALUES(NULL,'%s','%s','%s')" % (LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT))
	#֮ǰ��LINKд��LINT�ˣ������Ѿ��Ļ�����................................
	try:
	   # ִ��sql���
	   cursor.execute(sql_str)
	   # �ύ�����ݿ�ִ��
	   db.commit()
	except:
	   # �������������ع�
	   print("----Failed!!!")

	   #������ͣ���ڵ���
	   os.system("pause");
	   db.rollback()

	# �ر����ݿ�����
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


# �����ݿ�����
db = pymysql.connect("localhost","hyx","1154007hyx","LINKS")
# ʹ��cursor()������ȡ�����α�
cursor = db.cursor()
sql = ("DELETE FROM SINA_LINKS;")
# ִ��sql���
cursor.execute(sql)
# �ύ�����ݿ�ִ��
db.commit()
# �ر����ݿ�����
db.close()

for each in alink:
	if len(each.text) > 0:
		LINK_TEXT = each.text
		LINK_URL = each.get('href')
		print("LINK_TEXT = %s" % (LINK_TEXT))
		print("LINK_URL = %s" % (LINK_URL))
		if len(LINK_TEXT) > 5:
			#ֻ��ȡ����5���ֵ����ӵ���ϸ����
			target = LINK_URL
			link_req = requests.get(url = target)
			gbk_link = 'http://slide.news.sina.com.cn'
			if gbk_link in target:
				#GBK�����utf-8��������
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
					print("-----------------------------------��ƪ������ʼ-----------------------------------")
					begin_mark = 1

				p=each.text
				print(p)
				if con_mark==0:
					LINK_NEWS_CONTENT=p
					con_mark=1
				else:
					LINK_NEWS_CONTENT = LINK_NEWS_CONTENT+p


			if begin_mark==1:
				print("-----------------------------------��ƪ��������-----------------------------------")
				print("")
		else:
			LINK_NEWS_CONTENT = None
		#������
		insert_into(LINK_TEXT,LINK_URL,LINK_NEWS_CONTENT)
		#ʹ������������
		LINK_NEWS_CONTENT = None
		#���LINK_TEXT��LINK_URL��һ��Ҫ�л���
		print("")
print("......���")
