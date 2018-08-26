# Description
This is a spyder program for mobike location, you can get the location of mobikes of a certain area.
+ Use *GaoDe Coordinate System*
+ Location is stord in /mobike_loc-[date]-[time].csv

# Dependencies
+ Windows/Linux
+ Python2
```
import requests
import urllib3
import time
import csv
```

# Operation
+ Download the document and unzip tit
+ Run *requirements.txt*
+ Change the variable *location* in *mobike_spyder.py* with [GaoDe Coordinate System](https://lbs.amap.com/console/show/picker), it can be one or more than one point
```
location = [('120.262277', '31.488689'), ('120.268457', '31.488689')]
```
+ Run *mobike_spyder.py*

```
pip install -r requirements.txt
python mobike_spyder.py
```

# Output Format
+ csv

bikeid | biketype | time | longitude | latitude
------ | ------ | ------ | ------ | ------
000001 | 0 | 2018/7/01  10:00:00 | 120.26569092 | 31.48410353

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

Postman:
![postman]

result:
![result]

visualization(using online web visualization software [BDP](https://www.bdp.cn/home.html)):
![visualization]
