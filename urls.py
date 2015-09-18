from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

# from transtech_directory.views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
