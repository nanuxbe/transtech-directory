from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import urls as auth_urls

from django_comments import urls as comments_urls
from star_ratings import urls as star_ratings_urls

from transtech_directory.views import (DirectoryListView, DirectoryDetailView,
    DirectoryCreateView)
# from transtech_directory.views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DirectoryListView.as_view(), name='directory'),
    url(r'^new/$', DirectoryCreateView.as_view(), name='directory_create'),
    url(r'^view/(?P<slug>[\w-]+)/$', DirectoryDetailView.as_view(), name='directory_detail'),

    url(r'^comments/', include(comments_urls)),
    url(r'^ratings/', include(star_ratings_urls, namespace='ratings', app_name='ratings')),
    url(r'^accounts/', include(auth_urls)),
]
