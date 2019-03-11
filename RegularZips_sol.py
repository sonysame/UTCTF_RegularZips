#Exrex is a tool and python module that generates all matching strings to a given regular expression.
import os
import exrex
from zipfile import *


def extract_zip(file, password, count):

	print("GOOD")
	zip_ref = ZipFile(file)
	
	for i in password:
		try:
			zip_ref.extractall(pwd=i)
			print ("Found Password is  ...... : " + i + "\n")
			print(zip_ref.namelist())
			if os.path.exists('hint.txt'):
				f=open("hint.txt",'r')
				password=list(exrex.generate(f.readline()))
				f.close()
			if os.path.exists('archive.zip'):
				os.rename('archive.zip','archive'+str(count)+'.zip')
				if count>1:
					os.remove("archive"+str(count-1)+".zip")
			return password	

		except Exception, e:
			pass


if __name__ == '__main__':
	password=[]
	encZip='RegularZips.zip'
	password=list(exrex.generate("^	7	y	RU[A-Z]KKx2 R4\d[a-z]B	N$"))
	password=extract_zip(encZip, password,1)
	j=0
	while 1:
		j+=1
		try:
			password=extract_zip("archive"+str(j)+".zip",password,j+1)
		except:
			print("DONE")

