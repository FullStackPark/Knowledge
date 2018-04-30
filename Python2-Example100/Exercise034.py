#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：练习函数调用。
#程序分析：无。
def hello_world():
    print 'hello world'

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':         #__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话
                                   # 意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，
                                   # 代码块不被运行
    three_hellos()