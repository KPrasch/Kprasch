from instagram.client import InstagramAPI

instagram_photo_urls = []
api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
popular_media = api.media_popular(count=20)
for media in popular_media:
    instagram_photo_urls.extend([media.images['standard_resolution'].url])