# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/5/22 17:02
# File   : linkToJuniperEX.py
# IDE    : PyCharm

from pprint import pprint
from jnpr.junos import Device
dev = Device(host='172.16.100.31',user='lab',password='lab123',port='22')
dev.open()
pprint(dev.facts)
dev.close()