from datetime import date

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import momoko

from urls import application
 

if __name__ == "__main__":
    application.listen(8888)

    _io_loop = IOLoop.instance()

    application.db = momoko.Pool(
        dsn='dbname=canary user=cognical '
            'host=localhost port=5432',
        size=1,
        ioloop=_io_loop,
    )

    future = application.db.connect()

    _io_loop.add_future(future, lambda x: _io_loop.stop())
    _io_loop.start()
    future.result()

    http_server = HTTPServer(application)
    http_server.listen(8888, 'localhost')
    _io_loop.start()