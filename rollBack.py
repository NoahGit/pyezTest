# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/7/3 10:42
# File   : rollBack.py
# IDE    : PyCharm

#如何对指定juniper设备进行回滚操作
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='172.16.100.31',user='lab',password='lab123',gather_facts=False)
dev.open()

cu = Config(dev)
diff = cu.diff()  #Run a show |compare command
if diff:
    cu.rollback()
dev.close()