import urllib.request
import json
import os

def login():
        username = input("username:")
        password = input("password:")
        url = "https://api.zoomeye.org/user/login"
        data = json.dumps({'username':username,'password':password})
        data_bytes = bytes(data,'utf8')
        try:
                req = urllib.request.Request(url,data_bytes)
                response = urllib.request.urlopen(req)
                html = response.read().decode('utf-8')
                target = json.loads(html)
                
                access_token = target['access_token']
                with open('access_token.txt','w') as f:
                        f.write(access_token)
                        f.close
                        print('login seccess !!!')
                #print('your access_token is:%s'%(access_token))
        except Exception as err:
                print('[info]:username or password is wrong !')
                

def apiget():
        while True:
                host_or_web = input("search for host or web:(‘q!’Sign out):")
                if host_or_web == 'q!':
                        break
                query = input("input your keyword(-r for your resources-info):")
                if query == '-r':
                        req = urllib.request.Request('https://api.zoomeye.org/resources-info')
                        ida = open('access_token.txt').read() 
                                
                        req.add_header('Authorization','JWT %s'%(ida))
                        re = urllib.request.urlopen(req)
                        ae = (re.read().decode('utf-8'))
                        ae = target = json.loads(ae)
                        dict_web = ae['resources']['web-search']
                        dict_host = ae['resources']['host-search']
                        print('your web search:%s'%(dict_web))
                        print('your host search:%s'%(dict_host))
                else:
                        try:
                                
                                req = urllib.request.Request('https://api.zoomeye.org/%s/search?query=%s'%(host_or_web,query))
                                idb = open('access_token.txt').read() 
                                req.add_header('Authorization','JWT %s'%(idb))
                                r = urllib.request.urlopen(req)
                                a = (r.read().decode('utf-8'))
                                a = target = json.loads(a)
                                print('tatal:%s'%(a['total']))
                                for i in range(len(a['matches'])):
                                        print (a['matches'][i]['ip'])
                                
                                
                        except Exception as err:
                                print('[erro]:Please enter the correct syntax !')

                        
def start():
        if not os.path.isfile('access_token.txt'):
                print('[info]:you need login')
                login()
        
        apiget()
        
                       

        
if __name__ == '__main__':
    start()

                

        
        






