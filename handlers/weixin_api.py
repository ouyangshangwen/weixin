# coding=utf-8

from handlers.base import BaseHandler


class WechatCallbackAPI(BaseHandler):
    '''验证服务器地址有效性.

    '''

    def get(self):
        self.write("hello world")

    def check_signature(self):
        signature = self.get_argument("signature", " ")
        timestamp = self.get_argument("timestamp", " ")
        nonce = self.get_argument("nonce", " ")
