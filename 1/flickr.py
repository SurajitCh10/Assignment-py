import flickrapi

api_key = u'1fe6f837d35616536373d1cfb17e14bd'
api_secret = u'355a0a7cd173ee31'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
photos = flickr.photos.search(user_id='195608576@N03', per_page='10')
s = flickr.photosets.getList(user_id='195608576@N03')

print('set is: %s' % s)