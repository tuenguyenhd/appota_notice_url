from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.controller import GameUserResource
from api import controller

game_user_resource = GameUserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appota_notice_url.views.home', name='home'),
    # url(r'^api/$', controller.notice_url,name='notice_url'),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^controller/', include(game_user_resource.urls)),
)
