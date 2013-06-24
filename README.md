# ad map backend version 0.1

## Step

1.import advertisement places by excuting 'create_places.py' script.
  It will create record in mongo db

2.import advertisement by excuting 'create_ads.py' script.

3.match the ads and the places by excuting 'match_advertisement.py'

4.create the static js file resource by excuting 'create_file_resources.py'

5.create the static js file  'create_static_file.py'

6.upload to cloud(eg.upyun excuting 'upload_upyun.py')

## project folder structure

```
__src______
|		   |
|		   |_______libs (libraries)
|		   |
|		   |_______model (data models)
|		   |
|		   |_______persitence (database api)
|		   |
|		   |_______tools (utils)
|
|
|__data (json data,ads.json places.json ...)
|
|__static_files (/maptype/zoom/lng-lat.js)
|
|__conf (db-config...)	
```	

		