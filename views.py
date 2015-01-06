from instagram.client import InstagramAPI

api = InstagramAPI(client_id='MY_CLIENT_ID', client_secret='MY_CLIENT_SECRET')
recent_media= api.user_recent_media(my_user_id, 6, max_id)
for media in recent_media:
   print media.images['standard_resolution'].url