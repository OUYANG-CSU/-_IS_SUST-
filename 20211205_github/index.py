#This is a python3 index.py
#So we should know the basic grammar for the python3

#This is from Folders_Name import the xxx.py file 
from utils import Utils
from utils import User
import datetime
import time

#I just add crontab in my Aliyun ECS(System:Centos7.9) 
#So,i did not use the function getNowHourMinSec()
def getNowHourMinSec():
	
	d = datetime.datetime.now()
	hour = int(str(d)[11:13])
	minute = int(str(d)[14:16])
	seconds = int(str(d)[17:19])
	return hour,minute,seconds



if __name__ == '__main__':
	#i did not use the function getNowHourMinSec
	#Hours,Minutes,Seconds = getNowHourMinSec()
	#if Hours== 8 and Minutes == 2 or Hours == 23 and Minutes == 2:
	cookie = User.login()
	Utils.upload_ncov_message(cookie)
	#else:
	#time.sleep(30)
		
