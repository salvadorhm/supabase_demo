import web

from mvc.controllers.index import Index
from mvc.controllers.contactos import Contactos


web.config.debug = False

urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
