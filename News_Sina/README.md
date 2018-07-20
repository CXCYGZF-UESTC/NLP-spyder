# Description
This is a simple single threaded Python crawler, using BeautifulSoup to make simple links and news text crawling to Sina News homepage and store it in MySQL. To slightly improve the performance, the crawler crawls only the news text with more than five characters. It is important to note that this crawler does not exclude the picture description text, and the Sina picture news column http://slide.news.sina.com.cn/ uses GBK coding rather than UTF-8 encoding. The notes are Chinese and easy to understand.


# Dependencies
+ Windows 10
+ Python 3.6
+ MySQL 8.0

```
from bs4 import BeautifulSoup
import requests
import pymysql
import os
```

# Operation
+ Download MySQL, install it and sign in your account.
+ I recomand using MySQL 8.0 Command Line Client - Unicode to create your database and table.
+ Download sina_links.py and add it into your editor.
+ Install BeautifulSoup, requests and pymysql through pip(you can search for how to do it)
+ Replace some personal settings and run!