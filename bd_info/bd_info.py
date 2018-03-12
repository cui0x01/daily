#!/usr/bin/python3

import socket,time
client=socket.socket()

global logdate
logdate = time.strftime('%Y%m%d%H%M%S',time.localtime())

def w_log(file_name,data):
    with open(file_name+'.txt', 'a+') as f:
        f.write(data.decode())

def telnet():
    client.connect(("10.8.12.80", 343))  #获取刚链接上的信息
    if len(client.recv(1024))>=0:
        time.sleep(0.3)
        data1 = client.recv(1024)
        #print(data1.decode())

    client.send(b"admin\n")             #输入登录帐号接收信息
    if len(client.recv(1024))>=0:
        time.sleep(0.3)
        data2 = client.recv(1024)
        #print(data2.decode())

    client.send(b"admin\n")             #输入密码接收信息
    if len(client.recv(1024)) >= 0:
        time.sleep(0.3)
        data3 = client.recv(1024)
        #print(data3.decode())

def exec_cmd():
    client.send(b"show cpu\n")          #show cpu
    if len(client.recv(1024)) >= 0:
        time.sleep(0.3)
        data4 = client.recv(1024)
        #print(data4.decode())
        w_log(logdate,data4)

    client.send(b"show board all-all \n")   #show board all-all
    i=0
    while i<4:
        data5=client.recv(1024)
        time.sleep(0.2)
        #print(data5.decode())
        i=i+1
        w_log(logdate,data5)
    # if len(client.recv(1024))>=0:
    #     time.sleep(0.3)
    #     data10 = client.recv(1024)
    #     print(data10.decode())

    client.send(b"show switchover\n")
    i = 0
    while i < 2:
        data6 = client.recv(1024)
        time.sleep(0.2)
        #print(data6.decode())
        i = i + 1
    # if len(client.recv(1024))>=0:
    #     time.sleep(0.3)
    #     data6 = client.recv(1024)
        w_log(logdate,data6)


    client.send(b"show alarm all \n")
    i = 0
    while i < 5:
        data7 = client.recv(1024)
        time.sleep(0.2)
        #print(data7.decode())
        i = i + 1
        w_log(logdate,data7)

if __name__ == "__main__":
    telnet()
    exec_cmd()


client.close()
print("_____check_success_____")

