from django.contrib import admin
from django.conf.urls import url
from .import views

app_name='stories'

urlpatterns = [
    url(r'^$',views.story_list, name="list"),
    url(r'^new/$',views.story_new, name="new"),
    url(r'^(?P<slug>[\w-]+)/$', views.story_detail, name="detail"),
]
