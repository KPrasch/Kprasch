from PIL import Image
import os

from django.conf import settings
from django.shortcuts import render
from instagram.client import InstagramAPI


def main(request):
    from instagram.client import InstagramAPI

    access_token = "1483928180.10bb1f3.2aaef28f7ad943988b89fe42e56ed016"
    api = InstagramAPI(access_token=access_token)
    instagram_photo_urls = []
    recent_media, next_ = api.user_recent_media(user_id=1483928180, count=20) 
    for media in recent_media:
        instagram_photo_urls.extend([media.images['standard_resolution'].url])
    return render(request, 'base.html', {'instagram_photo_urls': instagram_photo_urls})

def gallery(request):
    images = os.listdir(os.path.join(settings.PROJECT_ROOT, "static/img/gallery/high_res"))
    #import pdb; pdb.set_trace()
    return render(request, 'gallery.html', {'images': images})

def make_thumbs(request):
    img_path = os.path.join(settings.PROJECT_ROOT, "static/img/gallery/high_res")
    size = (75,75)
    images = os.listdir(img_path)
    for image in images:
        Image.open(image).thumbnail(size).save(os.path.join(full_path, "thumbs/thumb_%s" % image))
    return render(request, 'gallery.html')
