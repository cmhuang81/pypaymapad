#-*- coding: utf-8 -*
import pymongo
import os

_here = os.path.dirname(__file__)

def create_file():
	connection = pymongo.Connection('localhost',27017)
	db = connection.paymapad
	frs = db.jsfileresources.find()
	for fr in frs:
		path = os.path.join(_here,"../static_files",str(fr['mapTypeID']),str(fr['zoom']))
		file_name = str(fr['filekey'])
		file_name = os.path.join(path,file_name+".js")
		# print file_name
		if not os.path.isdir(path):
			os.makedirs(path)
		file_content = fr['filecontent']
		file_content = "define({ \n"+fr['filecontent']+" \n]})"
		file_obj = open(file_name,"w")
		# print file_obj
		file_obj.write(file_content)
		file_obj.close()
	connection.close()


if __name__ == '__main__':
	create_file()
