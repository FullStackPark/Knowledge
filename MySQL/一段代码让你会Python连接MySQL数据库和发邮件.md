# 一段代码让你会Python连接MySQL数据库和发邮件

<!---->零度沸点 2017-09-30 21:40:08

![一段代码让你会Python连接MySQL数据库和发邮件](http://p3.pstatp.com/large/3c7a000450c6b2e724f2)

python

闲来无事写段Python脚本监控下数据库及查询网站是否正常，有异常可以发邮件警报，每10分钟自动检查一次

\# -*- coding: UTF-8 -*-

import requests

import sys, os, re, urllib, urlparse ,sched,time

import smtplib

import traceback

import MySQLdb

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from urllib import urlopen

\#上数引入所需的相应库

reload(sys)

sys.setdefaultencoding('gbk')

\#邮件函数

def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):

mail_msg = MIMEMultipart()

if not isinstance(subject,unicode):

subject = unicode(subject, 'utf-8')

mail_msg['Subject'] = subject

mail_msg['From'] =fromaddr

mail_msg['To'] = ','.join(toaddrs)

mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))

try:

s = smtplib.SMTP()

s.connect(smtpaddr)

s.login(fromaddr,password)

s.sendmail(fromaddr, toaddrs, mail_msg.as_string())

s.quit()

except Exception,e:

print "Error: unable to send email"

print traceback.format_exc()

def huizong():

try:

conn = MySQLdb.connect(host='MySQL数据库IP地址', port=端口号,user='用户名',passwd='密码',db='数据库')

cur=conn.cursor()

count = cur.execute('select 某一字段名 from 表名 limit 1')

results = cur.fetchall()

cur.close()

conn.close()

mysqlshuju=1 #如果能连接上，则该变量为1

except Exception as e:

mysqlshuju=0 #如果连接出现异常，则该变量为0

if mysqlshuju==0:

shuju2="数据库无法连接"

else:

shuju2="数据库连接正常"

f = open('url.txt', 'r')#url.txt为需要检查的网站的网址列表，格式需类似为http://www.baidu.com

url = f.readlines()

length = len(url)

url_result_success=[]

url_result_failed=[]

num = 0#定义一个num变量并初始化为0

for i in range(0,length):

try:

response = requests.get(url[i].strip(), verify=False, allow_redirects=True, timeout=5)

if response.status_code != 200:

\#由于检测的网站没有重定向，所以只考虑200的状态码，如果有重定向还需要考虑301、302等状态码

raise requests.RequestException(u"Status code error: {}".format(response.status_code))

except requests.RequestException as e:

url_result_failed.append(url[i])

num=1#如果无法连接到网址，将num变为1

continue

url_result_success.append(url[i])

f.close()

result_len = len(url_result_success)

failed_len = len(url_result_failed)

if mysqlshuju==0 or num==1:

fromaddr = "发送的邮箱地址" #例如XXXXX@126.com

smtpaddr = "smtp.126.com" #这个是使用126邮箱的

toaddrs = ["填写需要发送到的那个邮箱","填写发送的邮箱地址"]

subject = "在线监控邮件" #邮件标题

password = "XXXXXXX" #这个密码非邮箱登录密码，是开启smpt的时候设置的那个授权密码

msg=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))#获取下当前的时间

for i in range(0,failed_len):#做循环，把监控到无法访问的网址都列出来

msg += url_result_failed[i].strip()

msg+="网站无法访问"

msg+=shuju2

sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)

print shuju2.decode('UTF-8').encode('gbk')

else:

print shuju2.decode('UTF-8').encode('gbk')

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

for i in range(0,result_len):

print 'URL %s' % url_result_success[i].strip()+' '' ''success'

for i in range(0,failed_len):

print 'URL %s' % url_result_failed[i].strip()+' '' ''failed'

schedule = sched.scheduler(time.time, time.sleep)

def execute_command(cmd, inc):

\#os.system(cmd)

huizong()

\#print '1'

schedule.enter(inc, 0, execute_command, (cmd, inc))

def main(cmd, inc=600): #这个是定时的时间，单位是秒，目前是设置10分钟一次

schedule.enter(0, 0, execute_command, (cmd, inc))

schedule.run()

if __name__ == '__main__':

main("netstat -an", 600)

\#print code

里面的一些IP地址及账号和密码填写下，就可以正常运行了

但是监控到网址无法访问的时候只是那个点连接时候网站没响应，有可能下一秒就又好使了，所以下次还得优化下能够一段时间内平均下，就会好点。

![一段代码让你会Python连接MySQL数据库和发邮件](http://p9.pstatp.com/large/3c790003a9183dee438d)

在控制台中运行

![一段代码让你会Python连接MySQL数据库和发邮件](http://p3.pstatp.com/large/3c7f0000ba903523cffd)

邮箱收到的警报邮件
