#!/usr/bin/env python3
# coding=utf-8

import struct
import os
from socket import *
import re

while 1:
    filename = 'reset_log'
    server_ip = input('(输入q键退出)请输入IP:')
    if server_ip=='q':
        exit()
    def checkip(server_ip):
        pat = re.compile(r'([0-9]{1,3})\.')
        r = re.findall(pat, server_ip + ".")
        if len(r) == 4 and len([x for x in r if int(x) >= 0 and int(x) <= 255]) == 4:
            pass
        else:
            print('check your ip')
            exit()
    checkip(server_ip)
    send_data = struct.pack('!H%dsb5sb' % len(filename), 1, filename.encode('gb2312'), 0, 'octet'.encode('gb2312'), 0)
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(send_data, (server_ip, 69))  # 第一次发送, 连接服务器69端口
    s.settimeout(2)
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, 'ab')

    try:
        while 1:

            recv_data = s.recvfrom(1024)  # 接收数据
            caozuoma, ack_num = struct.unpack('!HH', recv_data[0][:4])  # 获取数据块编号
            rand_port = recv_data[1][1]  # 获取服务器的随机端口
            if int(caozuoma) == 5:
                print('服务器返回: 文件不存在...')
                os.remove(filename)
                break
            #print(caozuoma, ack_num, rand_port, len(recv_data[0]))
            f.write(recv_data[0][4:])
            if len(recv_data[0]) < 516:
                break

            ack_data = struct.pack("!HH", 4, ack_num)
            s.sendto(ack_data, (server_ip, rand_port))  # 回复ACK确认包
    except Exception as e:
        print('---check your ip---')
        print('---download fail---')
        os.remove(filename)
        exit()

    print('---download success---\n')