# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/5/24 16:33
# File   : sshPublicKeys.py
# IDE    : PyCharm

#如何获取juniper设备信息，通过ssh加密密钥,密码看不见
import getpass
from jnpr.junos import Device
from pprint import pprint

host = None
uname = None
pw = None
key_file = './id_rsa_EX'

if host == None:
    host = input("hostname or IP: ")
if uname == None:
    uname = input("Username: ")
if pw == None:
    pw = getpass.getpass("SSH private key pass phrase: ")

dev = Device(host=host, user=uname, password=pw, ssh_private_key_file=key_file)
dev.open()
pprint(dev.facts)
dev.close()