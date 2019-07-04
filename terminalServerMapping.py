# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/7/4 21:39
# File   : terminalServerMapping.py
# IDE    : PyCharm

#juniper对服务器的端口映射
from jnpr.junos import Device
from lxml import etree

print('Terminal Server Inventory')
count = 7007
while (count<7033):
    try:
        with Device(host='172.16.100.31',user='lab',password='lab123',
                    mode='telnet',port='count',gather_facts=True) as dev:
            junosinfo = dev.facts
            print('Hostname:'+junosinfo['hostname']+','+'Hardware:'+junosinfo['model']+','+
                  'Software:'+junosinfo['version']+','+'TermServPort:'+str(count))
    except:
        pass
    count = count+1