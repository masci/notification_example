from django.conf.urls import patterns, include, url

from notification.views import IndexView, MessagesView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^messages/$', MessagesView.as_view(), name='messages'),
    url(r'^api/', include('stored_messages.urls')),
)
