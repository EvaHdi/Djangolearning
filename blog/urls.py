"""
# -*- coding:utf-8 -*-
@Project : django_introduction
@File : urls.py
@Author : EvaHdi
@Time : 2023/9/4 23:04
"""

from django.urls import path, include

import blog.views


urlpatterns = [
    path('hello_world', blog.views.hello_world)
]
