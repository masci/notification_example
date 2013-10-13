from django.views.generic import TemplateView
from django.contrib.messages import add_message

import stored_messages


class IndexView(TemplateView):
    template_name = 'notification/homepage.html'

    def get_context_data(self, **kwargs):
        add_message(self.request, stored_messages.STORED_INFO, 'You visited the homepage')
        return super(IndexView, self).get_context_data(**kwargs)


class MessagesView(TemplateView):
    template_name = 'notification/messages.html'

    def get_context_data(self, **kwargs):
        add_message(self.request, stored_messages.STORED_INFO,
                    'You visited the notifications page')
        return super(MessagesView, self).get_context_data(**kwargs)
