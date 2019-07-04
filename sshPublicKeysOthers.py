# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/7/2 15:07
# File   : sshPublicKeysOthers.py.py
# IDE    : PyCharm

#如何批量获取juniper各个设备信息，密码是加密的形式
import getpass
from jnpr.junos import Device
from pprint import pprint
import sys
import argparse
import os

filenamePath = None
host = None
uname = None
pw = None
key_file = './id_rsa_mx80'

if filenamePath == None:
    filenamePath = input("Enter filenamePath:") #需要输入存ip地址的txt文件路径,比如E:\djangoProject\pyezTest\inventory.txt
if uname == None:
    uname = input("Username:")
if pw == None:
    pw = getpass.getpass("SSH private key pass phrase:")
with open(filenamePath) as f:
    for line in f:
        host = line.rstrip(os.linesep)
        dev = Device(host=host, user=uname, password=pw, ssh_private_key_file=key_file)
        dev.open()
        pprint(dev.facts)
        dev.close()