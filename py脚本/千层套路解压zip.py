#coding=utf-8
import os
import zipfile


orginal_zip = "0573.zip"

while True:
	tag = orginal_zip
	orginal_zip = zipfile.ZipFile(orginal_zip)
	for contents in orginal_zip.namelist():
		password = contents[0:contents.find('.')]
	print password
	orginal_zip.setpassword(tag[:-4])
	try:
		orginal_zip.extractall()
	except:
		break
	if(len(tag)>6):
		os.system("rm "+tag)
	orginal_zip=password+".zip"