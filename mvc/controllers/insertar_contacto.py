import os
import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render("mvc/views", base="template")


class InsertarContacto:

    # Renderiza el archivo insertar_contacto.html
    def GET(self):
        return render.insertar_contacto() # type: ignore

    # Recibe los input del formulario y accede a cada uno
    # utilizando el atributo 'name'
    def POST(self):
        # Accede a los datos del formuario 'contactos'
        formulario = web.input(foto={})
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']
        
        archivo = formulario['foto']
        foto = archivo.filename

        ruta = os.path.join("static/fotos/",foto)
        with open(ruta, "wb") as file:
            file.write(formulario.foto.file.read())

        model_contactos = ModelContactos()
        datos = model_contactos.insertarContacto(nombre,email,telefono,foto)

        html = """
            <h1>Contacto almacenado correctamente</h1>
            <a href='/contactos'>Regresar</a>
        """
        return html

