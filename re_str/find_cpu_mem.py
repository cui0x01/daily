'''
@time:18-3-20 下午8:21
@Author:cui0x01
'''

import os,json,re

def find_str(str):
    a=[]
    res1=re.findall("Active SCMIP2 CPU usage :(.+?)%",str.strip())
    a.append(res1)
    res2=re.findall("Active SCMIP2 MEM usage :(.+?)%",str.strip())
    a.append(res2)
    res3=re.findall("Standby SCMIP2 CPU usage :(.+?)%",str.strip())
    a.append(res3)
    res4=re.findall("Standby SCMIP2 MEM usage :(.+?)%",str.strip())
    a.append(res4)
    return a

def find_file():
    abs_path=os.path.abspath("")
    file_list=sorted(os.listdir(abs_path))
    if os.path.exists('find_cpu_mem.txt'):
        os.remove('find_cpu_mem.txt')
    #print(file_list)
    for each in file_list:                      #得到每个文件的名字
        if ".txt" and "2018" in each:
            with open(str(each), 'r') as f:
                each_content=f.readlines()     #读取内容
                #print(each_content)
                res=find_str(json.dumps(each_content))    #正则查找字符串
                #print(type(res))
                res.insert(0,each)
                res=json.dumps(res)
                #print(type(res))
                with open('find_cpu_mem.txt','a+') as f:
                    f.write(res+'\n')
find_file()