from django.views.generic import TemplateView, FormView
from django.contrib.messages import add_message
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse

import stored_messages


class IndexView(FormView):
    template_name = 'notification/homepage.html'
    form_class = AuthenticationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        add_message(self.request, stored_messages.STORED_INFO, 'You visited the homepage')
        return super(IndexView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(IndexView, self).form_valid(form)


class MessagesView(TemplateView):
    template_name = 'notification/messages.html'

    def get_context_data(self, **kwargs):
        add_message(self.request, stored_messages.STORED_INFO,
                    'You visited the notifications page')
        return super(MessagesView, self).get_context_data(**kwargs)
