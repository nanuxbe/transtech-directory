from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from django_comments import urls as comments_urls

from transtech_directory.views import DirectoryListView

# from transtech_directory.views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='transtech_directory/index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^directory/$', DirectoryListView.as_view(), name='directory'),
    url(r'^comments/', include(comments_urls)),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]
