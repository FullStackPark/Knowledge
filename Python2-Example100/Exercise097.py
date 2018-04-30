#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
if __name__ == '__main__':
    from sys import stdout
    filename = raw_input('输入文件名:\n')
    fp = open(filename,"w")
    ch = raw_input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)                      #??这一行的存在意义，不是上面一行已经写入了吗
        ch = raw_input('')
    fp.close()