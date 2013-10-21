from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.messages import add_message

import stored_messages


def _user_logged_in(*args, **kwargs):
    add_message(kwargs['request'], stored_messages.STORED_INFO, 'You were logged in!')
user_logged_in.connect(_user_logged_in)


def _user_logged_out(*args, **kwargs):
    add_message(kwargs['request'], stored_messages.STORED_INFO, 'You were logged out!')
user_logged_out.connect(_user_logged_out)
