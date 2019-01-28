import tornado.ioloop
import tornado.web
import importlib as imp
import sys
from interpreter import run


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', result="", code="", data="")

    def post(self):
        code = self.get_argument('code')
        try:
            result = run(code)
        except:
            result = "Ошибка..."
        self.render('index.html', result=result, code=code)


routes = [
    (r"/", MainHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'}),
    (r'/src-min-noconflict/(.*)', tornado.web.StaticFileHandler, {'path': 'src-min-noconflict'}),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
