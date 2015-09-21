from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from django_comments import urls as comments_urls

from transtech_directory.views import (DirectoryListView, DirectoryDetailView,
    DirectoryCreateView)
# from transtech_directory.views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DirectoryListView.as_view(), name='directory'),
    url(r'^new/$', DirectoryCreateView.as_view(), name='directory_create'),
    url(r'^view/<?P(slug)[\w-]+>/', DirectoryDetailView.as_view(), name='directory_detail'),

    url(r'^comments/', include(comments_urls)),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]
