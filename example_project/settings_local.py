#!/usr/bin/env python
# encoding: utf-8
import sys
from settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASEDIR, 'example.sqlite')
}

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.append(
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append(
    'debug_toolbar'
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
