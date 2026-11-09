import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:

    def GET(self):

        model_contactos = ModelContactos()

        # Almacena en datos los registros recibidos de Supabase
        datos = model_contactos.obtenerContactos()

        #print(datos)

        # Envia a contactos.html los datos de supabase
        return render.contactos(datos) # type: ignore
