'''
@time:3/18/18 2:40 PM
@Author:cui0x01
'''
import socket,time,paramiko
client=socket.socket()

global logdate
logdate = time.strftime('%Y%m%d%H%M%S',time.localtime())

filename=logdate+".txt"
def w_log(file_name,data):
    with open(file_name+'.txt', 'a+') as f:
        f.write(data)

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
        w_log(logdate,data4.decode())
    print("==>exec show cpu")

    client.send(b"show board all-all \n")   #show board all-all
    i=0
    while i<4:
        data5=client.recv(1024)
        time.sleep(0.2)
        #print(data5.decode())
        i=i+1
        w_log(logdate,data5.decode())
    # if len(client.recv(1024))>=0:
    #     time.sleep(0.3)
    #     data10 = client.recv(1024)
    #     print(data10.decode())
    print("==>exec show board")

    client.send(b"show switchover\n")
    i = 0
    while i < 2:
        data6 = client.recv(1024)
        time.sleep(0.2)
        #print(data6.decode())
        i = i + 1
        w_log(logdate,data6.decode())
    print("==>exec show switchover")

    client.send(b"show alarm all \n")
    i = 0
    while i < 5:
        data7 = client.recv(1024)
        time.sleep(0.2)
        #print(data7.decode())
        i = i + 1
        w_log(logdate,data7.decode())
    print("==>exec show show alarm")
    client.close()
    #print(client) 检查socket是否关闭

#so add/delete
def sub_opreat():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("10.8.12.80", 22, "admin", "admin")
    command = {
        1: "cresub n:0998082200 anw:1280genew l3addr:200 analog",
        2: "cresub n:0998082201 anw:1280genew l3addr:201 analog",
        3: "delsub n:0998082200",
        4: "delsub n:0998082201",
    }

    for k in command:
        print(command[k])
        w_log(logdate,command[k]+"\n")
        stdin, stdout, stderr = ssh.exec_command(command[k])
        time.sleep(0.3)
        #print(stdout.read().decode("gbk"))
        res=stdout.read()
        w_log(logdate,res.decode("gbk"))
    ssh.close()


if __name__ == "__main__":
    telnet()
    print("==>telnet success")
    exec_cmd()
    sub_opreat()

print("filename:%s download success"%filename)

