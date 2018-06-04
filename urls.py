import tornado.web

from views import (DeviceHandler, DeviceLoadHandler)


application = tornado.web.Application([
    (r"/device/", DeviceHandler),
    (r"/device/preload/", DeviceLoadHandler)
], debug=True)