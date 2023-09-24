import cherrypy
from os.path import abspath
import string

def app():
    return open("index.html")
app.exposed = True

CP_CONF = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./') # staticdir needs an absolute path
            }
        }


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8082})
    cherrypy.quickstart(app, '/', CP_CONF)