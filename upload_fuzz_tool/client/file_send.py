# -*- coding: utf-8 -*-
#@Time      :2018/7/14 9:39
#@Author    :cui0x01
#@file      :webshell_send.py


from requests_toolbelt import MultipartEncoder
import requests
import time
import os
import sys
import getopt

global logdate
logdate = time.strftime('%Y%m%d%H%M%S',time.localtime())
def w_log(data):
    '''

    :return:
    '''
    if not os.path.exists('log'):
        os.mkdir('log')
    log_name=os.path.join('log',logdate)
    with open(log_name,'a+') as f:
        f.write(data)

def send_url(url,folder):
    '''

    :return:
    '''
    abs_path = os.path.abspath(os.path.dirname(__file__))
    folder_path=os.path.join(abs_path,folder)
    try:
        file_list= os.listdir(folder_path)
    except BaseException as re:
        print('''
        %s is not exist, please check your folder.
        '''%folder)
        os._exit(0)
    for filename in file_list:
        #print(filename)
        #print(url)
        m = MultipartEncoder(
            fields={'uploaded': (filename, open(os.path.join(folder_path,filename), 'rb'), 'text/plain')}
        )
        '''
        Content-Disposition:form-data; name="uploaded"; filename="aa.php"
        这里的files里uploaded   就是multipart协议name字段里面的uploaded
        服务端也是根据isset( $_FILES[ 'uploaded' ]，multipart协议name字段里面的uploaded接收文件。
        如果修改，要保持一致。
        '''
        #print(len(files))
        time.sleep(1)
        #file=os.path.join(folder_path,filename)
        #new_url=url+filename
        try:
            r = requests.post(url, data=m,headers={'Content-Type': m.content_type})
        except BaseException as re:
            print('waf reject: filename %s'%filename)
            data='waf reject: filename %s \n'%filename
            w_log(data)

        else:
            print("waf allow: filename: %s"%filename)
            data="waf allow: filename: %s \n"%filename
            w_log(data)



if __name__ == "__main__":

    try:
        opts,args=getopt.getopt(sys.argv[1:],'u:f:')
        u=opts[0][1]
        f=opts[1][1]
        #print(u,f)
    except Exception as e:
        print('''
        ******************************************************************
        ex:python2 xx.py -u http://33.33.35.20/upload/upload.php -f white
        -u: target url                                                   
        -f: local folder                                                 
        ******************************************************************
        ''')
        os._exit(0)
    send_url(u,f)