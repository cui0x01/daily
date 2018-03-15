#coding: utf-8
'''
z = zipfile.ZipFile('') , extractall
z.extractall(pwd)
'''
import zipfile
import threading

def zipbp(zfile, pwd):
	try:
		zfile.extractall(pwd=pwd)
		print 'password found : %s' % pwd
	except:
		return
def main():
	zfile = zipfile.ZipFile('test.zip')
	pwdall = open('password.txt')
	for pwda in pwdall.readlines():
		pwd = pwda.strip('\n')
		t = threading.Thread(target=zipbp, args=(zfile, pwd))
		t.start()
		t.join()
if __name__ == '__main__':
	main()
