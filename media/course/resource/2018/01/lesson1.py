# -*- coding: utf-8 -*-

#请将字符串“1234[[xyz]]5678[[abcd]]90[[ttkk]]mmnn”中，[[]]中的字符取出来，并打印。提示：使用查找和截取字符串操作。
#请思考一下字符串操作中find和index的区别
#提示：使用字符串查找和截取


def get_postion(src,flag_start,flag_end):
    pos_start = src.find(flag_start)
    pos_end = src.find(flag_end)

    return {"start" : pos_start, "end" : pos_end }


str = "1234[[xyz]]5678[[abcd]]90[[ttkk]]mmnn"

flag_start = "[["
flag_end = "]]"

pos = get_postion(str, flag_start, flag_end)

while (pos["start"] != -1) and (pos["end"] != -1):
    sub = str[pos["start"] + len(flag_start): pos["end"]]
    print("sub:" + sub)
    str = str[ pos["end"] + len(flag_end): len(str)]
    print("str:" + str)

    pos = get_postion(str, flag_start, flag_end)
