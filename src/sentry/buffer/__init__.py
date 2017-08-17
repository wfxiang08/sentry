# -*- coding:utf-8 -*-
from __future__ import absolute_import

from django.conf import settings

from sentry.utils.services import LazyServiceWrapper

from .base import Buffer  # NOQA


backend = LazyServiceWrapper(Buffer, settings.SENTRY_BUFFER,
                             settings.SENTRY_BUFFER_OPTIONS)
# 将内部变量直接暴露成为可以直接访问的变量
backend.expose(locals())
