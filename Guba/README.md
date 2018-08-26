# Description
* This is a project to crawl the stock review website. 
* In the project, I climbed all the comments on the 300 stocks in the HS300 index from January 1, 2015 to the present.
* I use the framework: pyspider and database operations: mongoDB.


# Dependencies
+ [pyspider](http://docs.pyspider.org/en/latest/)(framework)
+ [mongoDB](https://www.mongodb.com/)/[redis](https://redis.io/)(database)
+ lxml/datatime/re

```
import re
import datetime
from pymongo import *
from lxml import etree
from pyspider.libs.base_handler import *
```

# Operation

+ Download [pyspider](http://docs.pyspider.org/en/latest/)(framework), [mongoDB](https://www.mongodb.com/), [redis](https://redis.io/) and other dependencies.
+ run `set_stockCodes/setCodes.py`（in order to get all symbols of HS300 and load them into mongoDB）
+ put `set_database/resultdb.py` into database/mongodb directory of pyspider（in order to save the crawling data to mongoDB）
+ start **redis**
+ command line run `pyspider -c config.json all &` under directory of `config.json`
+ copy script in script folder, paste code to your own project in localhost:5000, save
+ click run button in localhost:5000
+ Complete two last steps before the market is open, then you'll get sentiment data everyday periodically.






# Output Format
* You'll find a collection named [date]Guba under a database called [stockcode]eastmoney.
* And you will have **documents** like:
```
{
'_id': ObjectId('5b51f174c1fb25567d5eba1e'), 
'taskid': 'da01f5291f17de702d1bd7ec02d00757', 
'author': '股友5Soa6g', 
'comment': '0', 
'create': '2017-03-20 11:49:56', 
'created_at': 618916962, 
'last': '03-20 11:49', 
'read': '1240', 
'text': 'A股糸统行情都轰轰烈烈慢悠悠像是名路神仙消受不起，水土不服。', 
'title': 'A股糸统行情都轰轰烈烈慢悠悠像是名路神仙消受', 
'url': 'http://guba.eastmoney.com/list,000001,f_344.html'
}
```

# Something important:
1. This project is a very good chance to be familiar with the framework--*pyspider* and the operations of using the *mongoDB*.
2. The two frameworks of spider(pyspider & scrapy) have their own advantages and disadvantages. I recommend to start with pyspider and learn about scrapy later, because pyspyider is more visible for developers.
3.333
4. **Last but not least, the spider is just a tool, we need to get the data in the shortest time and with the least effort.**
