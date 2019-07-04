# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/5/22 22:15
# File   : interactiveInput.py
# IDE    : PyCharm

#如何获取juniper设备的设备信息,密码是以明文的形式展示出来
import getpass
from pprint import pprint
from jnpr.junos import Device

host = None
uname = None
pw = None

if host == None:
    host = input("Hostname or IP:")
if uname == None:
    uname = input("Username:")
if pw == None:
    pw = getpass.getpass()
dev = Device(host=host, user=uname, password=pw)
pprint(pw)
dev.open()
pprint(dev.facts)
dev.close()