from django.conf.urls import patterns, url

from api import controller

urlpatterns = patterns('',
    url('notice_url_ios_appvn', controller.notice_url_ios_appvn, name='notice_url_ios_appvn'),
    url('notice_url_ios_itunes', controller.notice_url_ios_itunes, name='notice_url_ios_itunes'),
    url('notice_url_android_appvn', controller.notice_url_android_appvn, name='notice_url_android_appvn'),
    url('notice_url_android_gplay', controller.notice_url_android_gplay, name='notice_url_ios_gplay'),
)
