# coding=utf-8
"""
    WiFi Web 应用入口
    =================

"""

import os

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options


from configs import AppSettings
from handlers import  weixin_api

# Options
define("port", default=9982, help="run on the given port", type=int)



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", weixin_api.WechatCallbackAPI),


        ]

        settings = dict(
            cookie_secret="CPetensssabcdefgas*&@$&23022234348147@!$^*d8964",
            debug=True,
            autoreload=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),

        )
        tornado.web.Application.__init__(self, handlers, **settings)


def AppStart(port=None):
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)  # Port to listen
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    print "************* start **************"
    AppStart()