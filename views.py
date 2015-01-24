from instagram.client import InstagramAPI
from django.shortcuts import render

def main(request):
    instagram_photo_urls = []
    api = InstagramAPI(client_id='10bb1f3d107946698142fa3d859a8a26', client_secret='d9c0181c35cb473cb8b9ad858517eee1')
    recent_media = api.user_recent_media(1483928180, 20, 20)
      
    #for media in recent_media:
    #    import pdb; pdb.set_trace()
    #    instagram_photo_urls.extend([media.images['standard_resolution'].url])
     
    return render(request, 'base.html', instagram_photo_urls)