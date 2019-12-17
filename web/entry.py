# _*_coding:utf-8_*_
"""
@ProjectName: TornadoFramwork
@Author:  Javen Yan
@File: entry.py
@Software: PyCharm
@Time :    2019/12/5 上午10:39
"""
from __future__ import print_function
import tornado.web
from web.settings import *
from web.urls import urlpatterns


def make_app(login_handler, log_func, **settings):
    settings['template_path'] = sys_templates
    settings['static_path'] = sys_static
    settings['cookie_secret'] = sys_secret
    settings['login_url'] = sys_login_url
    settings['debug'] = sys_debug
    settings['static_url_prefix'] = sys_static_url_prefix
    settings['autoreload'] = sys_auto_reload
    settings['jwt_expire'] = sys_jwt_expire
    settings['log_function'] = log_func

    urlpatterns.append((r"{}".format(sys_login_url), login_handler))
    return tornado.web.Application(urlpatterns, **settings)
