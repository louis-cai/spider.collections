url https://app.qichacha.net/app/v1/admin/checkLoginType?telNo=17057295997&timestamp=1467946747542&sign=67e779ec43f8ac4712ce82330866ea45e4fe56c4

GET /app/v1/admin/checkLoginType?telNo=17057295997&timestamp=1467946747542&sign=67e779ec43f8ac4712ce82330866ea45e4fe56c4 HTTP/1.1
Authorization: Bearer ZjUzYmExMDAtY2Q2Zi00N2NlLTliNTUtMzM4ZTU5MWY4YzBk
Host: app.qichacha.net
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.2.0


telNo	17057295997
timestamp	1467946747542
sign	67e779ec43f8ac4712ce82330866ea45e4fe56c4


---

	HTTP/1.1 200 OK
Server	Tengine
Content-Type	application/json; charset=utf8
Transfer-Encoding	chunked
Connection	keep-alive
Content-Encoding	gzip
Date	Fri, 08 Jul 2016 02:59:08 GMT
Via	cache19.l2et15[29,200-0,M], cache16.l2et15[30,0], kunlun10.cn143[103,200-0,M], kunlun10.cn143[104,0]
X-Cache	MISS TCP_MISS dirn:-2:-2
X-Swift-SaveTime	Fri, 08 Jul 2016 02:59:08 GMT
X-Swift-CacheTime	0
Timing-Allow-Origin	*
EagleId	7cc1cd8a14679467482074525e



{
	"status": 200,
	"message": "成功",
	"result": {
		"checkFlag": 1,
		"userFaceImg": "http://share.qichacha.com/app-new/home-news/images/default-head.png"
	}
}