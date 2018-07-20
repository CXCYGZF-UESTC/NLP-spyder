# Description
This is a project to crawl the stock review website. In the project, I climbed all the comments on the 300 stocks in the HS300 index from January 1, 2015 to the present. In this project I use the framework: pyspider and database operations: mongoDB.


# Dependencies
+ [pyspider(framework)](http://docs.pyspider.org/en/latest/)
+ mongoDB/redis(database)
+ lxml/datatime/re

```
import re
import datetime
from pymongo import *
from lxml import etree
from pyspider.libs.base_handler import *
```

# Operation

+ Download [pyspider(framework)](http://docs.pyspider.org/en/latest/)，[mongoDB](https://www.mongodb.com/)，[redis](https://redis.io/) and other dependencies.
+ run `set_stockCodes/setCodes.py`（in order to get all symbols of HS300 and load them into mongoDB）
+ put `set_database/resultdb.py` into database/mongodb directory of pyspider（in order to save the crawling data to mongoDB）
+ start **redis**
+ command line run `pyspider -c config.json all &` under directory of `config.json`
+ copy script in script folder, paste code to your own project in localhost:5000, save
+ click run button in localhost:5000
+ Complete two last steps before the market is open, then you'll get sentiment data everyday periodically.






# Output Format
You'll find a collection named [date]GuYouHui under a database called [stockcode]eastmoney.


# Other Things
About how to write this program, the main process is :
1. Use *Fiddler* to capture the packets of mobike app
2. Get the url and data form from the captured packets
3. Use *Postman* to simulate the spyder program and debug

# PS
Screenshots of each step:

[fiddler]: screenshots/fiddler.png
[Postman]: screenshots/postman.png
[result]: screenshots/result.png
[visualization]: screenshots/visualization.png
Fiddler:
![fiddler]

Postman:
![postman]

result:
![result]

visualization(using online web visualization software [BDP](https://www.bdp.cn/home.html)):
![visualization]
