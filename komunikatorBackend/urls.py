from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'komunikatorBackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup', 'komunikatorBackend.views.sign_up', name='sign_up'),
    url(r'^signin', 'komunikatorBackend.views.sign_in', name='sign_in'),
    url(r'^new_message', 'komunikatorBackend.views.new_message', name='new_message'),
)
