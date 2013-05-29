#-*- coding: utf-8 -*
import pymongo
import math
from tools import util

connection = pymongo.Connection('localhost',27017)

db = connection.paymapad


def create_staticInMongo():
	adPlacesList = db.adplaces.find()
	for adp in adPlacesList:
		filekey = util.keyMaker(adp['centerLnglat'][0],adp['centerLnglat'][1],adp['zoom'])
		fileResource = db.jsfileresources.find({'filekey':filekey})
		if fileResource:
			print "yes"
		else:
			print "no"	
		print filekey


if __name__ == '__main__':
	create_staticInMongo()
