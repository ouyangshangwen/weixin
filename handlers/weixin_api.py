# coding=utf-8

import hashlib
import urllib2
import urllib
import json

import tornado.httpclient
import  tornado.web

from handlers.base import BaseHandler
from configs import AppSettings
from utils import logs_general


class WechatCallbackAPI(BaseHandler):
    '''验证服务器地址有效性.

    '''

    def get(self):
        if self.check_signature():
            echostr = self.get_argument("echostr", "")
            self.set_header("Content-Type", "text/plain")
            self.write(echostr)
        else:
            self.write("")

    def check_signature(self):
        signature = self.get_argument("signature", " ")
        timestamp = self.get_argument("timestamp", " ")
        nonce = self.get_argument("nonce", " ")
        token = AppSettings.TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list_sorted = sorted(tmp_list)
        tmp_str = "".join(tmp_list_sorted)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return True
        else:
            return False

class UserInfoHandler(BaseHandler):
    """ 获取用户信息。

    """
    @tornado.web.asynchronous
    def get(self):
        code = self.get_argument("code", "")
        appid = AppSettings.APPID
        secret = AppSettings.SECRET
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (appid, secret, code)
        httpClient = tornado.httpclient.AsyncHTTPClient()
        request = tornado.httpclient.HTTPRequest(url=url)
        httpClient.fetch(request, self.on_response)

    def on_response(self, response):
        access_token = ""
        openid = ""
        if response.code == 200:
            try:
                resp_dict = json.loads(response.body)
                access_token = resp_dict["access_token"]
                openid = resp_dict["openid"]

            except Exception as e:
                logs_general.warning(str(e))
                self.write("failure")
            	self.finish()
                return

            data = urllib.urlencode(dict(
                                         access_token=access_token,
                                         openid=openid,
                                         lang="zh_CN"
                                             ))
            url = "https://api.weixin.qq.com/sns/userinfo?" + data

            httpClient = tornado.httpclient.AsyncHTTPClient()
            request = tornado.httpclient.HTTPRequest(url=url)
            httpClient.fetch(request, self.get_userinfo)

    def get_userinfo(self, response):
        if response.code == 200:
            try:
                resp_dict = json.loads(response.body)
            	self.render("userinfo.html", **resp_dict)
            except Exception as e:
                logs_general.warning(str(e))
                self.write("failure")
            	self.finish()
                return
        else:
            self.write("failure")
            self.finish()




