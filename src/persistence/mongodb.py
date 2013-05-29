#-*- coding: utf-8 -*
from __future__ import division
import pymongo
import math
from tools.util import *
import json
from bson.objectid import ObjectId

import ConfigParser



cf = ConfigParser.ConfigParser()
cf.read('../conf/db_config.ini')
db_host = cf.get("baseconf","host")
db_port = int(cf.get("baseconf","port"))

def create_staticInMongo():
    connection = pymongo.MongoClient(db_host,db_port)
    db = connection.paymapad
    adPlacesList = db.adplaces.find()
    i = 0
    for adp in adPlacesList:
        #print "i------------------",i
        mapTypeID = adp['mapTypeID']
        zoom = adp['zoom']
        filekey = keyMaker(adp['centerLnglat'][0],adp['centerLnglat'][1],zoom,mapTypeID)
        fileResource = db.jsfileresources.find_one({'filekey':filekey,'mapTypeID':mapTypeID})
        if not fileResource:
            # print "no"
            filecontent = create_content(filekey,adp)
            filecontent = '''id: "'''+filekey+'''",\nads:['''+filecontent
            db.jsfileresources.insert({'filekey':filekey,'filecontent':filecontent,'mapTypeID':mapTypeID,'zoom':zoom})
        else:            
            filecontent = fileResource['filecontent']+",\n"+create_content(filekey,adp)
            fileResource['filecontent'] = filecontent
            db.jsfileresources.update({"_id":fileResource["_id"]},fileResource)
        i = i+1
        print "completed-------------------------",i
        # print fileResource
    # db.close()
    connection.close()


def create_places(places):
	connection = pymongo.MongoClient(db_host,db_port)
	db = connection.paymapad
	i = 0
	for place in places:
		p = db.places.find_one({"rightBottomLnglat":place['rightBottomLnglat'], 
			"leftTopLnglat" : place['leftTopLnglat'], 
			"centerLnglat" : place['centerLnglat'], 
			"zoom" : place['zoom'], 
			"mapShapeID" : place['mapShapeID'], 
			"mapTypeID" : place['mapTypeID']})
		if p is None:
			db.places.insert(place)
		# print 'insert NO.',i
		i=i+1
		print 'completed----------------',i
	connection.close()

def create_ads(ads):
    connection = pymongo.MongoClient(db_host,db_port)
    db = connection.paymapad
    i = 0
    for ad in ads:
        name = ad['name']
        link = ad['link']
        lng = float(ad['xpoint'])
        lat = float(ad['ypoint'])
        icon = ad['icon']
        image = ad['image']
        a = db.ads.find_one({"name":name, 
            "lnglatArr" : [lng,lat], 
            "infoDescription" :[name,name,name]
            })
        if a is None:
            imgUrl = icon.replace("./", "http://pic.paymapad.com/")
            bigImgUrl = image.replace("./", "http://pic.paymapad.com/")
            ia = {}
            ia['name']= name
            ia['cateID']= 2
            ia['link']=link
            ia['lnglatArr']=[lng,lat]
            ia['imgUrl']=[imgUrl,imgUrl,imgUrl]
            ia['infoStyleID']=1
            ia['infoImgUrl']=[bigImgUrl,bigImgUrl,bigImgUrl]
            ia['infoDescription']=[name,name,name]
            db.ads.insert(ia)
        # print 'insert NO.',i
        i=i+1
        print 'completed----------------',i
    connection.close()

def match_ads():
    connection = pymongo.MongoClient(db_host,db_port)
    db = connection.paymapad
    ads = db.ads.find()
    for ad in ads:
        adLnglat = ad['lnglatArr'][0]
        # print db.places.find_one({'centerLnglat':{'$within':{'$centerSphere':[adLnglat, 1 / 3959]}}}).explain()
        place = db.places.find_one({'centerLnglat':{'$within':{'$centerSphere':[adLnglat, 1 / 3959]}}})
        if place:
            imgUrl = ad['imgUrl'][place['mapShapeID']]
            print imgUrl
            if not imgUrl:
                continue
            adplace = {}
            adplace['title'] = ad['name']
            adplace['link'] = ad['link']
            adplace['centerLnglat'] = place['centerLnglat']
            adplace['imgUrl'] = imgUrl
            adplace['mapShapeID'] = place['mapShapeID']
            adplace['mapTypeID'] = place['mapTypeID']
            adplace['infoImgUrl'] = ad['infoImgUrl']
            adplace['infoDescription'] = ad['infoDescription']
            adplace['infoStyleID'] = ad['infoStyleID']
            adplace['zoom'] = place['zoom']

            db.adplaces.insert(adplace)        	


if __name__ == '__main__':
	match_ads()
