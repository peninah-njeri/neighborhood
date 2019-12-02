from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url('^$',views.homepage, name ='homepage'),
    url(r'^post/',views.post,name='post'),
    url(r'^business/',views.business,name='business'),
    url(r'^neighbourhood/(\d+)',views.neighbourhood,name='neighbourhood'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)