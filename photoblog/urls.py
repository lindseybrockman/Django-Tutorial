from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# FOR LOCAL FILE SERVING:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photoblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^post/', include('post.urls')),
    url(r'^admin/', include(admin.site.urls)),

# FOR LOCAL FILE SERVING!
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)