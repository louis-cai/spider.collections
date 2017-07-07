# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

url = domain + "/CheckCodeCaptcha?currentTimeMillis=1468920570872&num=53800"
url = domain + "/CheckCodeYunSuan?currentTimeMillis=1469006544608&r=0.30482869976727156"

import requests


def downloadImageFile(imgUrl, local_filename):
    # local_filename = imgUrl.split('/')[-1]
    print "Download Image File=", local_filename
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    with open("data/img/" + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename


if __name__ == "__main__":
    for i in range(100):
        filename = "%d.jpg" % i
        downloadImageFile(url, filename)
