# NLP-spyder
This is a repository for spyder projects maintained by members of WIE.
## project introductions:
* This is an **index** of all projects.<br/> 
* For more complex projects, there are more detailed descriptions and operating instructions in the **folder**.

### Guba（股吧）：
* **URL：** <br/> 
http://guba.eastmoney.com/
* **Developer：**<br/> 
Haojun Gao
* **Description：**<br/> 
This is a project to crawl the stock review website. In the project, I climbed all the comments on the 300 stocks in the HS300 index from January 1, 2015 to the present. In this project I use the framework: pyspider and database operations: mongoDB.
* **Dependencies：**<br/> 
pyspider / mongoDB / redis / lxml / datatime / re
* **Operation：**<br/> 

### Sina Weibo（新浪微博）：
* **URL：**<br/> 
https://weibo.com/
* **Developer：**<br/> 
Zhiqi Liu
* **Description：**<br/> 
This code was designed for 'sina weibo', which is used to grap the content of certain weibo's comment. The only thing you have to do is to decide the range of each user's uid. This code can search user's uid in certain range. But remember that the address shouldn't have Chinese strings.
* **Dependencies：**<br/> 
python3.6
* **Operation：**<br/> 

### Bilibili（哔哩哔哩动画）：
* **URL：** <br/> 
https://www.bilibili.com/
* **Developer：**<br/> 
Wei Sun
* **Description：**<br/> 
This is a code that can automatically perform corresponding operations on the Bilibili station. The operations that can be performed are following, sending the bullet screen, making comments and saving to favorites.
* **Dependencies：**<br/> 
urllib / requests / ssl / re / time
* **Operation：**<br/> 
Input parameters: av_num （为所需要操作的视频的AV号）; <br/> 
send user settings: headers, headers1, csrf （通过更改cookie可以修改发送请求的用户）

### News_Sina（新浪新闻）：
* **URL：**<br/> 
http://news.sina.com.cn/
* **Developer：**<br/> 
Yexi Huang
* **Description：**<br/> 
This is a simple single threaded Python crawler, using BeautifulSoup to make simple links and news text crawling to Sina News homepage and store it in MySQL. To slightly improve the performance, the crawler crawls only the news text with more than five characters. It is important to note that this crawler does not exclude the picture description text, and the Sina picture news column http://slide.news.sina.com.cn/ uses GBK coding rather than UTF-8 encoding. The notes are Chinese and easy to understand.
* **Dependencies：**<br/> 
Python 3.6 / MySQL 8.0 / bs4 / requests / pymysql / os
* **Operation：**<br/> 
Download MySQL, install it and sign in your account.<br/> 
I recomand using MySQL 8.0 Command Line Client - Unicode to create your database and table.<br/> 
Download sina_links.py and add it into your editor.<br/> 
Install BeautifulSoup, requests and pymysql through pip(you can search for how to do it)<br/> 
Replace some personal settings and run!<br/> 

### Mobike（摩拜单车）：
* **Developer：**<br/> 
Yuzan Liu
* **Description：**<br/> 
This is a spyder program for mobike location, you can get the location of mobikes of a certain area.
* **Dependencies：**<br/> 
Windows/Linux<br/> 
Python2
* **Operation：**<br/> 
For more detailed operations, please open the readme in the folder mobike.
