# coding: utf-8

from django.conf.urls import include, patterns, url
from django.contrib import admin
from blog import feed
from info.views import index, pages
from django.conf.urls.static import static # относится к ckeditor
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^info/', include('info.urls', namespace='info')),
    url(r'^errors/', include('errors.urls', namespace='errors')),
    url(r'^forms/', include('myforms.urls', namespace='my_forms')),
    url(r'^ideator/', include('ideator.urls', namespace='ideator')),
    url(r'^context/', include('context.urls', namespace='context')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^pages/(\d{1,3})/$', pages),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$', index),
    url(r'^model/', include('modelsform.urls')),
    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += patterns('',
        url(r'^ckeditor/', include('ckeditor_uploader.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
