# coding=utf-8

import hashlib

from handlers.base import BaseHandler
from configs import AppSettings


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
