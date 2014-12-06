from django.conf.urls import url

from post.views import index, post

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<post_id>\d+)/$', post)
]
