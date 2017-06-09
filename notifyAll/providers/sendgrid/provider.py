#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.sendgrid.provider
~~~~~~~~~~~~~~

- This file contains the functionality of SendGrid Provider
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import get_connection

# local

# own app
from notifyAll.providers import base


class SendGridProvider(base.EmailProvider):
    """SendGrid Provider Class

    """
    id = 'sendgrid'
    name = 'SendGrid'

    def __init__(self, host, username=None, password=None, *args, **kwargs):
        """
        we will provide to ways to configure clients :
         - One, you can configure plivo keys from settings if not,
         - Then Second, you ca send keys as function arguments too,
         - Priority wil be given to function arguments

        :param sendgrid_api_key: SendGrid API key
        """
        super(SendGridProvider, self).__init__( *args, **kwargs)

        # connection related settings
        self.username = username
        self.password = password
        self.host = host
        # # validate necessary settings are configured by user for SendGrid
        # if sendgrid_api_key is None:
        #     sendgrid_api_key = getattr(settings, 'SENDGRID_API_KEY', None)
        #
        # if sendgrid_api_key is None:
        #     raise ImproperlyConfigured(
        #         'to send emails via {0} you need to configure SENDGRID_API_KEY in settings.'.format(self.name)
        #     )

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(self.notification_type)
        self.notify()

    def _make_connection(self):
        """make connection with backend

        :return: connection with email provider
        """
        configuration = {
            'username': self.username,
            'password': self.password,
            'host': self.host
        }

        return get_connection(backend=settings.EMAIL_BACKEND,
                              fail_silently=self.fail_silently,
                              **configuration)

RegisterProvider = SendGridProvider
