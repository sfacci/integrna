from django.conf.urls import patterns, include, url
#from django.contrib import admin
import dbquery
from dbquery import views


urlpatterns = patterns('',
    # Examples:
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    #url(r'^admin/', include(admin.site.urls)),
    
    #the main directory for app dbquery
    url(r'^$', dbquery.views.index, name="index"),
    url(r'^search/',include('dbquery.urls',namespace="dbquery")),
)
