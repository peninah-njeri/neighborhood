from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url('^$',views.homepage, name ='homepage'),
    url(r'^post/',views.post,name='post'),
    url(r'^business/',views.business,name='business'),
    url(r'^neighbourhood/(\d+)',views.neighbourhood,name='neighbourhood'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^businessdetails/(\d+)',views.businessdetails,name ='businessdetails'),
    url(r'^new/comment$',views.new_comment,name='comment'),
    url(r'^comments$',views.comments,name='comments'),
    url(r'^contacts/',views.contacts,name='contacts'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^edit/profile$',views.edit_profile,name='edit-profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^update/neighborhood$',views.update_neighborhood,name='update-neighborhood'),
    url(r'^update/profile/(\d+)',views.update_profile,name='update-profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)