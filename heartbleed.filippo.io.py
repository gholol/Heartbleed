import web
import subprocess as sp
import json

urls = (
    '/bleed/(.*)', 'bleed',
    '/test', 'test',
    '/.*', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        raise web.found('http://fil.io/Heartbleed')

class test:
    def GET(self):
        return ''

class bleed:
    def GET(self, host):
        web.header('Access-Control-Allow-Origin', '*')
        if not ':' in host: host += ':443'

        child = sp.Popen(['./heartbleed', host], stdout=sp.PIPE)
        data = child.communicate()[0]
        rc = child.returncode

        return json.dumps({'code': rc, 'data': data})

if __name__ == "__main__":
    app.run()
