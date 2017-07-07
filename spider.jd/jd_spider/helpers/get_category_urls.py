# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json, re
import codecs

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def read_json_file(file):
    return json.load(codecs.open(file, 'r', 'utf-8'))


def write_json_file(file, json_obj):
    json.dump(json_obj, codecs.open(file, 'w', 'utf-8'), ensure_ascii=False)


def do_format(in_obj):
    # in_obj = json.loads(in_text)

    data = in_obj.get("data")

    out_data = []
    out_data2 = []

    for d in data:
        id = d.get("id")
        s = d.get("s")

        for s_d in s:
            n1 = s_d.get("n")
            s1 = s_d.get("s")
            # style1 = s_d.get("style")

            for s1_d in s1:
                n2 = s1_d.get("n")
                s2 = s1_d.get("s")
                # style2 = s1_d.get("style")

                for s2_d in s2:
                    n3 = s2_d.get("n")
                    s3 = s2_d.get("s")
                    # style3 = s1_d.get("style")
                    if len(s3) > 0:
                        raise Exception("s3 > 0, error")

                    out_name = id + "." + n1.split('|')[1] + "." + n2.split('|')[1] + "." + n3.split('|')[1]

                    if len(n3.split('|')[0].split('-')) in [2, 3]:
                        url = "http://list.jd.com/list.html?cat=" + n3.split('|')[0] + "&go=0"
                    else:
                        url = "http://" + n3.split('|')[0]
                    print out_name, url
                    # print type(out_name)

                    out_d = {
                        "category": out_name,
                        "url": url
                    }
                    # print json.dumps(out_d)
                    if url.find("list") > 0:
                        out_data.append(out_d)
                    else:
                        out_data2.append(out_d)

    # print out_data
    return {"data1": out_data, "data2": out_data2}


def main():
    in_file = "../analysis/category.json"
    out_file = "../analysis/category_urls.json"
    print "in_file: ", in_file
    print "out_file: ", out_file
    try:
        print "----------start-------------"
        in_json = read_json_file(in_file)
        # print "do_format..."
        out_json = do_format(in_json)
        # print out_json
        write_json_file(out_file, out_json)
        print "----------Done-------------"
    except Exception, e:
        print e.message
        pass

if __name__ == '__main__':
    main()