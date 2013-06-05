#-*- coding: utf-8 -*
import json
from persistence.mongodb import create_places




if __name__ == '__main__':
    json_file = file('../data/ads.json')
    json_data = json.load(json_file)
    create_ads(json_data)
    json_file.close()