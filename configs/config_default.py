# coding=utf-8

import os

class AppSettingsDefault(object):
    '''默认设置。

    '''

    APPID = "APPID"
    SECRET = "SECRET"
    TOKEN =  "TOKEN"
    current_pach = os.path.split(os.path.abspath(__file__))[0]
    PROJECTPATH = os.path.split(current_pach)[0]