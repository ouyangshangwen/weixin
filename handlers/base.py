# coding=utf-8

import arrow
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    '''BaseHandler.

    '''

    def prepare(self):
        utcnow = arrow.utcnow().to("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss")
        method = self.request.method
        uri = self.request.uri
        print("\n\n---- Start ---- %s %s @ %s" % (method, utcnow,
                                                  uri))
    def on_finish(self):
        utcnow = arrow.utcnow().to("Asia/Shanghai").format("YYYY-MM-DD HH:mm:ss")
        method = self.request.method
        uri = self.request.uri
        print("\n\n---- End ---- %s %s @ %s" % (method, utcnow,
                                                  uri))