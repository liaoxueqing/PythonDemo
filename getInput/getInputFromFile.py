#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read()
print "读取的字符串是:\n", str
# 关闭打开的文件
fo.close()