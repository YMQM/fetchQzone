from django.conf.urls import patterns,url
from fetchQzone import views
urlpatterns=patterns('',
    #url(r'^$',views.indexView,name='index'),
    url(r'^search/$',views.upload,name='upload'),
    url(r'^search2/$',views.search),
    url(r'^onefeed/$',views.feedDetail),
    )