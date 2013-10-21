from django.conf.urls import patterns, include, url

from notification.views import IndexView, MessagesView


urlpatterns = patterns('',
    url(r'^logout/$', 'django.contrib.auth.views.logout',  {'next_page': '/'}, name='logout'),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^messages/$', MessagesView.as_view(), name='messages'),
    url(r'^api/', include('stored_messages.urls')),
)
