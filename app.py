import web

from mvc.controllers.index import Index
from mvc.controllers.contactos import Contactos
from mvc.controllers.insertar_contacto import InsertarContacto
from mvc.controllers.ver_contacto import VerContacto


web.config.debug = False

urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
    '/insertar_contacto','InsertarContacto',
    '/ver_contacto/(.*)','VerContacto',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
