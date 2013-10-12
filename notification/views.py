from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'notification/homepage.html'


class MessagesView(TemplateView):
    template_name = 'notification/messages.html'
