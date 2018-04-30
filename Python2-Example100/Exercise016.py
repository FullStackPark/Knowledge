#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：输出指定格式的日期。
#程序分析：使用 datetime 模块。
#strftime()方法语法：time.strftime(format[, t])，format - 格式字符串，t -可选的参数t是一个struct_time对象。
#返回以可读字符串表示的当地时间
import datetime

if __name__ == '__main__':   #__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ ，当模块被直接运行
                             # 时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    print(datetime.date.today().strftime('%d/%m/%Y'))# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看
                                                      # strftime() 方法
    miyazakiBirthDate = datetime.date(1941, 1, 5)     # 创建日期对象
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1) # 日期算术运算，使用datetime模块
                                                                          # timedelta实现日期时间相加
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1) # 日期替换
    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
