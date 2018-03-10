import os
import shutil
def find_file_path():
    if os.path.exists("abs_path.txt"): os.remove("abs_path.txt")
    path_list=[]
    dir_list=os.listdir(r"F:\BaiduNetdiskDownload\python全栈")
    for dir in dir_list:
        folder=r"F:\BaiduNetdiskDownload\python全栈\\"+dir
        path_list.append(folder)
        if os.path.isdir(folder):
            file_list=os.listdir(folder)
            for file_name in file_list:
                abs_path=[]
                rar='.rar'
                zip='.zip'
                if rar in file_name or zip in file_name:
                    tmp_path=folder+'\\'+file_name
                    with open('abs_path.txt','a+') as f:
                        f.write(tmp_path+'\n')
def copy_file():
    with open('abs_path.txt','r') as f:
        for old_path_name in f:
            print(old_path_name.strip()+'       -----down------')
            old_path_name=old_path_name.strip()
            file_name = old_path_name.split('\\')
            new_path_name=r'D:\python全栈笔记\\'+file_name[-1]
            shutil.copy(old_path_name,new_path_name)
    print('-------all_copy_down------------')
find_file_path()
#copy_file()



