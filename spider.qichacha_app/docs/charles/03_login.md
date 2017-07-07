url https://app.qichacha.net/app/v1/admin/login

	POST /app/v1/admin/login HTTP/1.1
Authorization	Bearer ZjUzYmExMDAtY2Q2Zi00N2NlLTliNTUtMzM4ZTU5MWY4YzBk
Content-Type	application/x-www-form-urlencoded
Content-Length	183
Host	app.qichacha.net
Connection	Keep-Alive
Accept-Encoding	gzip
User-Agent	okhttp/3.2.0


loginType	2
accountType	1
account	17057295997
password	0e031dcac2bfa6decad46f54abeac50e
identifyCode	
key	
token	
timestamp	1467946825024
sign	92c2c3d83ef6bdaa6847f4ea920ba26eec3a49c0


-----


	HTTP/1.1 200 OK
Server	Tengine
Content-Type	application/json; charset=utf8
Transfer-Encoding	chunked
Connection	keep-alive
Content-Encoding	gzip
Date	Fri, 08 Jul 2016 03:00:25 GMT
Via	cache10.l2et15[113,200-0,M], cache12.l2et15[113,0], kunlun10.cn143[260,200-0,M], kunlun8.cn143[261,0]
X-Cache	MISS TCP_MISS dirn:-2:-2
X-Swift-SaveTime	Fri, 08 Jul 2016 03:00:25 GMT
X-Swift-CacheTime	0
Timing-Allow-Origin	*
EagleId	7cc1cd9a14679468255004391e


{
	"status": 201,
	"message": "成功",
	"result": {
		"userInfo": {
			"uid": "1653236",
			"guid": "574d2af0a86c280043000228",
			"name": "",
			"nickname": "adhhd",
			"phone": "17057295997",
			"email": "",
			"groupid": "11",
			"qqopenid": "",
			"sinaid": "",
			"weixinid": "",
			"unionid": "",
			"user_type": "1",
			"sex": "0",
			"faceimg": "0",
			"is_comment": "1",
			"device_token": "Ai6EVqgFdIUFD-lX6_VQgXfeqAMSGtpfsxL_PTytbN5R",
			"invite_code": "",
			"last_login_time": "1467900731",
			"last_login_ip": "222.129.237.194",
			"regist_time": "1464675077",
			"regist_ip": "121.69.42.30",
			"last_remind_time": "0",
			"is_active": "1",
			"points": "0",
			"client_type": "2",
			"status": "1",
			"balanceId": "497788",
			"balance": "0.00"
		},
		"token": {
			"access_token": "NWM3NGZkZDktMTIzYS00NTdhLTg1NzMtOThiOGU5YzFlNWE5",
			"token_type": "Bearer",
			"expires_in": 3600,
			"refresh_token": "ff59da54cd6067a153c30c1abf973c6a"
		}
	}
}