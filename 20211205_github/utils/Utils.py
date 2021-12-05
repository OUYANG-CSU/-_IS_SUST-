#This is Utils.py
import requests
import json

#i got the DEFAULT_HEADER using the google chrome(F12),
#Notice: The DEFAULT_HEADER here is different from the DEFAULT_HEADER from User.py
#You should change the DEFAULT_HEADER 
DEFAULT_HEADER = {
	"Accept": "application/json, text/plain, */*",
	"Accpet-Encoding": "gzip,deflate,br",
	"Accept-Language": "en-US,en;q=0.9",
	"User-Agent":	"Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
	"Referer": "https://app.sust.edu.cn/site/ncov/dailyup/",
	"Origin": "https://app.sust.edu.cn"
}

wlc_upload_url = "https://app.sust.edu.cn/ncov/wap/open-report/save"

wlc_upload_msg = {
	"sfzx": "1",
	"tw": "1",
	"area": "陕西省 西安市 未央区",
	"city": "西安市",
	"province": "陕西省",
	"address": "陕西省西安市未央区未央湖街道陕西科技大学食品与生物工程学院陕西科技大学西安校区",
	"geo_api_info":"{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"fEa\":\"jsonp_731268_\","
									 "\"position\":{\"Q\":34.37692,\"R\":108.97414000000003,\"lng\":108.97414,\"lat\":34.37692},"
									 "\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\","
									 "\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"029\","
									 "\"adcode\":\"610112\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
									 "\"building\":\"\",\"buildingType\":\"\",\"street\":\"显庆路\",\"streetNumber\":\"29号\","
									 "\"country\":\"中国\",\"province\":\"陕西省\",\"city\":\"西安市\",\"district\":\"未央区\","
									 "\"towncode\":\"610112012000\",\"township\":\"未央湖街道\"},\"formattedAddress\":\"陕西省西安市未央区未央湖街道陕西科技大学食品与生物工程学院陕西科技大学西安校区\","
									 "\"roads\":[],\"crosses\":[],\"pois\":[]}",
	"sfcyglq": "0",
	"sfyzz": "0",
	"qtqk":	"",
	"ymtys": ""
}

def upload_ncov_message(cookie):
	header = DEFAULT_HEADER
	r = requests.post(wlc_upload_url,cookies=cookie,headers=header,data=wlc_upload_msg)
	if r.json()['e'] == 0:
		print("wlc upload succeed")
		return "Upload success"
	else:
		print("wlc upload failed{}".format(r.json()['m']))
		return "Upload failed"

