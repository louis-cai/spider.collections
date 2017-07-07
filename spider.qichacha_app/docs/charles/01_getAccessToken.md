
url	https://app.qichacha.net/app/v1/admin/getAccessToken
SSl TLSv1.2 (TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)
Content-Type application/json; charset=utf8
Method POST

POST /app/v1/admin/getAccessToken HTTP/1.1
Content-Type	application/x-www-form-urlencoded
Content-Length	183
Host	app.qichacha.net
Connection	Keep-Alive
Accept-Encoding	gzip
User-Agent	okhttp/3.2.0

appId	80c9ef0fb86369cd25f90af27ef53a9e
deviceId	V00IG/C/9fsDAFLGppYaSufx
version	9.0.3
deviceType	android
os	
timestamp	1467946511126
sign	71f2ffe734220d8e937b3ff5481d6e645548579a


---

HTTP/1.1 200 OK
Server: Tengine
Content-Type: application/json; charset=utf8
Transfer-Encoding: chunked
Connection: keep-alive
Content-Encoding: gzip
Date: Fri, 08 Jul 2016 02:55:11 GMT
Via: cache9.l2et15[58,200-0,M], cache20.l2et15[59,0], kunlun8.cn143[115,200-0,M], kunlun10.cn143[116,0]
X-Cache: MISS TCP_MISS dirn:-2:-2
X-Swift-SaveTime: Fri, 08 Jul 2016 02:55:11 GMT
X-Swift-CacheTime: 0
Timing-Allow-Origin: *
EagleId: 7cc1cd8a14679465109795427e

{
	"status": 201,
	"message": "注册成功",
	"result": {
		"access_token": "ZjUzYmExMDAtY2Q2Zi00N2NlLTliNTUtMzM4ZTU5MWY4YzBk",
		"token_type": "Bearer",
		"expires_in": 3600,
		"refresh_token": "ff59da54cd6067a153c30c1abf973c6a"
	}
}