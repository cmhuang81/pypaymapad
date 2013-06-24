#-*- coding: utf-8 -*
import math
from string import Template

import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read('../conf/db_config.ini')
db_host = cf.get("mongodbconf","host")
db_port = int(cf.get("mongodbconf","port"))

# google tile
def getFileKey(lon, lat, nZoom):
    x = int(math.floor((float(lon) + 180) / 360 * math.pow(2, nZoom)))
    y = int(math.floor((1 - math.log(math.tan(lat * math.pi / 180) + 1 / math.cos(lat * math.pi / 180)) / math.pi) / 2 * math.pow(2, nZoom)))
    return [x, y, nZoom]


def keyMaker(lon,lat, nZoom,mapTypeID):
    key = getFileKey(lon,lat,nZoom)
    return str(mapTypeID)+"-"+str(key[2])+"-"+str(key[0])+"-"+str(key[1])

content_template = Template('''{
"id":"${id}",
"title":"${title}",
"link":"${link}",
"imgUrl":"${imgUrl}",
"infoImgUrl":"${infoImgUrl}",
"infoDescription":"${infoDescription}",
"centerLnglat":[ ${x}, ${y} ],
"zoom":${z},
"mapTypeID":${mapTypeID},
"mapShapeID":${mapShapeID},
"infoStyleID":${infoStyleID}
}''')

def create_content(filekey,adp):
	return content_template.substitute(id=filekey,title=adp['title'],link=adp['link'],
		imgUrl=adp['imgUrl'],infoImgUrl=adp['infoImgUrl'],infoDescription=adp['infoDescription'],
		x=str(adp['centerLnglat'][0]),y=str(adp['centerLnglat'][1]),
		z=adp['zoom'],mapTypeID=adp['mapTypeID'],mapShapeID=adp['mapShapeID'],
		infoStyleID=adp['infoStyleID'])





