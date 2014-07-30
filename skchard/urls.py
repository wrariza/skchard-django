from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from blog.views import PostViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skchard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

)
