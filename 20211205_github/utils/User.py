#This is the User.py
import pickle
import requests
import os
import json

#get the DEFAULT_HEADER from google chrome(F12),you must know what i said
#You should change the DEFAULT_HEADER
DEFAULT_HEADER = {
	"Accept": "application/json,text/javascript,*/*;q=0.01",
	"Accept-Encoding": "gzip,deflate,br",
	"Accept-Language": "en-US,en;q=0.9",
	"Connection": "keep-alive",
	"Content-Length": "27",
	"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
	"X-Requested-With": "WMLHttpRequest"
}

#You shoule change the wlc_login_url
wlc_login_url = "https://app.sust.edu.cn/uc/wap/login/check"

#You shoule change the wlc_cookie_file_name and wlc_config_path
#i use the absolute path for this The /root/IS_SUST/... on my Aliyun ECS
wlc_cookie_file_name = "/root/IS_SUST/data/cookie.txt"

wlc_config_path = "/root/IS_SUST/data/config.json"

def	get_cookie_from_login(student_id:	str,	password:	str,wlc_cookie_file_path=wlc_cookie_file_name):
	r = requests.post(wlc_login_url,data={"username":student_id,"password":password},headers=DEFAULT_HEADER)
	if r.status_code == 200:
		if r.json()['e'] == 0:
			print("wlc Login succeed")
			with open(wlc_cookie_file_name,'wb') as f:
				pickle.dump(r.cookies,f)
			return r.cookies
		else:
			print(r.json()['m'])
			raise RuntimeError("wlc Login failed")


def load_cookie_from_file(wlc_cookie_file_path=wlc_cookie_file_name):
	with open(wlc_cookie_file_path,'rb')as f:
		return pickle.load(f)


def login():
	_cookies = ""
	if os.path.exists(wlc_cookie_file_name):
		_cookies = load_cookie_from_file(wlc_cookie_file_name)
	else:
		wlc_config_file = open(wlc_config_path,'r',encoding="utf-8")
		config = json.load(wlc_config_file)
		stu_num = config["stuNum"]
		password = config["passWord"]
		_cookies = get_cookie_from_login(stu_num,password)
	return _cookies
