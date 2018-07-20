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
For more detailed operations, please open the readme in the folder `Guba`.

### Sina Weibo（新浪微博）：
* **URL：**<br/> 
https://weibo.com/
* **Developer：**<br/> 
Zhiqi Liu
* **Description：**<br/> 
This code was designed for 'sina weibo', which is used to grap the content of certain weibo's comment. The only thing you have to do is to decide the range of each user's uid. This code can search user's uid in certain range. But remember that the address shouldn't have Chinese strings.
* **Dependencies：**<br/> 
python3.6

### Bilibili（哔哩哔哩动画）：
* **URL：** <br/> 
https://www.bilibili.com/
* **Developer：**<br/> 
Wei Sun
* **Description：**<br/> 
This is a code that can automatically perform corresponding operations on the Bilibili station. The operations that can be performed are following, sending the bullet screen, making comments and saving to favorites.
* **Dependencies：**<br/> 
urllib / requests / ssl / re / time


### News_Sina（新浪新闻）：
* **URL：**<br/> 
http://news.sina.com.cn/
* **Developer：**<br/> 
Yexi Huang
* **Description：**<br/> 
This is a simple threaded Python crawler, using BeautifulSoup to make links and news text crawling to Sina News homepage and store it in MySQL. To slightly improve the performance, the crawler crawls only the news text with more than five characters.
* **Dependencies：**<br/> 
Python 3.6 / MySQL 8.0 / bs4 / requests / pymysql / os
* **Operation：**<br/> 
For more detailed operations, please open the readme in the folder `News_Sina`.

### Mobike（摩拜单车）：
* **Developer：**<br/> 
Yuzan Liu
* **Description：**<br/> 
This is a spyder program for mobike location, you can get the location of mobikes of a certain area.
* **Dependencies：**<br/> 
Windows/Linux<br/> 
Python2
* **Operation：**<br/> 
For more detailed operations, please open the readme in the folder `mobike`.
