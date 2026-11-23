# 3.1 Especificación de Requerimientos: Aplicación Web Segura Agenda v23.11.2026.3

## 1. Objetivo

Desarrollar una aplicación web bajo el patrón arquitectónico MVC, implementando autenticación de usuarios, control de acceso basado en sesiones persistentes y protección de parámetros en URL mediante firmas HASH para prevenir ataques de enumeración (IDOR).

## 2. Reglas de Negocio y Seguridad Transversales (RNT)



### RNT01 - Protección de rutas privadas

1. Todas las vistas y controladores del **Módulo 2** (**index**, **lista_contactos**, **ver_contacto**, **insertar_contacto**, **actualizar_contacto**, **borrar_contacto**) deben validar antes de ejecutarse que exista una **cookie** / **variable de sesión** activa y que el **token** coincida con un registro vigente en la tabla **sesiones_abiertas** de Supabase.
2. Si la validación falla, el sistema debe redirigir inmediatamente a login.

### RNT02 - Generación y validación de URLs firmadas (HASH)

1. Ningún identificador numérico (**id_contacto**) debe exponerse sin firma en las URLs.
2. El sistema generará una firma **HMAC/HASH** combinando el **id_contacto** y una **SECRET_KEY**  bajo el formato "**id_contacto:HASH**" (en memoria, sin alterar la llave primaria en la base de datos).

## 3. Requerimientos Técnicos y Tecnológicos (RTT)

### RTT01 - Stack Tecnológico y Arquitectura

* **Backend**:

    1. **Lenguaje de programación**: Python 3.12
    2. **Practicas de implementación**: Tipado estático, manejo de excepciones enumeradas mediante bloques **try/except** y **logging** usando **logging.getLogger(__name__)** en cada módulo para su identificación.
    3. **Framework web**: Microframework **web.py**
    3. **Arquitectura**: Patrón arquitectónico **Modelo-Vista-Controlador** (MVC) con controladores  de acción única (**login.py**, c**errar_sesion.py**, **index.py**, **lista_contactos.py**, **ver_contacto.py**, **insertar_contacto.py**, **actualizar_contacto.py**, **borrar_contacto.py**).

* **Frontend**:
    1. HTML5 semántico.
    2. CSS3.
    3. JavaScript vanilla.
    4. La renderización de vistas será mediante el motor de plantillas integrado de web.py (**web.template.render**), usando la plantilla base **template.html** donde se define el maquetado de todo el módulo, y cada vista se enfoca unicamente en su funcionalidad.

### RTT02 - Integración con Backend as a Service (Supabase)

* **Librería de conexión**:

    1. SDK oficial de supabase para Python **supabase**, configurado mediante variables de entorno (**SUPABASE_URL** y **SUPABASE_KEY**) en el archivo **.env**.
    2. El acceso a las variables de entorno mediante la librería **dotenv**.

* **Servicios utilizados**:

    1. **Supabase Authentication**: Autenticación básica de Email y Password, usando la validación de credenciales de acceso (**sign_in_with_password**) y gestión de **tokens JWT** de sesión.
    2. **Supabase Database** (**PostgreSQL**): Persistencia de datos mediante consultas parametrizadas desde la capa de **Modelo** hacia las tablas contactos y sesiones_abiertas.

### RTT03 - Estructura de Datos (Esquema de Base de Datos)

La base de datos en Supabase debe contener las siguientes entidades principales:
1. Tabla **contactos**:
    * **id_contacto** (int / bigint, Primary Key, autoincremental).
    * **nombre** (varchar / text, obligatorio: Almacena el nobre completo del contacto).
    * **email** (varchar / text, obligatorio: Almacena el email del contacto).
    * **telefono** (varchar / text, obligatorio: Almacena el teléfono del contacto).
    * **foto** (varchar / text, obligatorio: Almacena el nombre del archivo de imagen).

2. Tabla **sesiones_abiertas**:
    * **token** (varchar / text, obligatorio: Almacena los tokens activos JWT de los usuarios autenticados), usado para validar la vigencia de cada petición contra la **cookie o variable de sesión** de **web.py**.

### RTT04 - Gestión de Archivos Estáticos (Imágenes)

* **Almacenamiento local**:
    1. Las fotografías de los contactos se almacenarán en el sistema de archivos local del servidor dentro del directorio **static/fotos/**.

* **Integridad de archivos**:

    1. Al insertar o actualizar un contacto con imagen, el sistema validará la extensión del archivo (.jpg, .jpeg, .png, .webp) y guardará el archivo en **static/fotos/** evitando colisiones de nombres con un **timestamp** para el nombre del archivo.
    2. Al actualizar la fotografía o eliminar un contacto (**RF07** y **RF08**), el servidor eliminará el archivo físico correspondiente en **static/fotos/** (verificando previamente su existencia con **os.path.exists** y omitiendo imágenes por defecto).

### RTT05 - Seguridad y Protección de URLs

1. **Firma criptográfica** (**Anti-IDOR**): El módulo de seguridad empleará la librería estándar **hmac** y **hashlib** (Usar el algoritmo **SHA256**), utilizando una **CLAVE_SECRETA** para generar y verificar las cadenas **id_contacto:HASH** en todas las operaciones de consulta, actualización y borrado.

2. **Control de sesiones**: Uso del gestor de sesiones de web.py (**web.session**) respaldado por la validación cruzada contra el campo token de la tabla **sesiones_abiertas** en Supabase en cada solicitud a rutas protegidas.

## 4. Módulo 1: Autenticación y Gestión de Sesiones

### RF01 - Inicio de sesión (login)

* **Descripción**: Permite a un usuario registrado autenticarse en el sistema.

* **Flujo principal**:

    1. El usuario ingresa su email y contraseña en el formulario de la vista login.
    2. El controlador envía las credenciales al servicio **Authentication** de Supabase.
    3. Si las credenciales son válidas, el sistema obtiene el **token de sesión** generado por Supabase, lo almacena en una **cookie segura o variable de sesión**, registra el token en la tabla **sesiones_abiertas** de Supabase y redirige a la página de bienvenida (index).

* **Flujo alternativo (Error)**:

    1. Si las credenciales son inválidas, el sistema permanece en login y muestra el mensaje: "**Credenciales incorrectas, verifique sus datos**".

### RF02 - Cerrar sesión (cerrar_sesion)

* **Descripción**: Finaliza de forma segura la sesión activa del usuario.

* **Flujo principal**:

    1. El usuario selecciona el enlace de cerrar sesión.
    2. El controlador **cerrar_sesion** elimina el registro del token correspondiente en la tabla sesiones_abiertas de Supabase.
    3. El sistema destruye la cookie o variable de sesión local y redirige a la vista login.

## 5. Módulo 2: Gestión de Contactos (CRUD)

### RF03 - Página de bienvenida (index)

* **Descripción**: Punto de entrada tras la autenticación exitosa.

* **Flujo principal**:

    1. Muestra un mensaje de bienvenida al usuario autenticado, un enlace para navegar a la lista de contactos (**lista_contactos**) y la opción para cerrar sesión (**cerrar_sesion**).

### RF04 - Lista de contactos (lista_contactos)

* **Descripción**: Muestra el catálogo completo de contactos registrados con enlaces protegidos para cada acción.

* **Flujo principal**:

    1. El controlador consulta todos los registros de la tabla **contactos** en Supabase (id_contacto, nombre, email, telefono, foto).
    2. En controlador, recorre cada registro y calcula su HASH aplicando la fórmula **id_contacto:HASH** (usando el id_contacto y la palabra **CLAVE_SECRETA** del servidor).
    3. La vista renderiza una tabla con las columnas: **Foto**, **Nombre**, **Email**, Teléfono y Acciones (enlaces a ver_contacto, actualizar_contacto y borrar_contacto pasando el parámetro **id_contacto:HASH ** en la URL).
    4. Incluye un botón o enlace visible "**INSERTAR**" para ir a **insertar_contacto**.

### RF05 - Ver detalle de contacto (ver_contacto)

* **Descripción**: Muestra la información completa de un contacto específico.

* **Flujo principal**:

    1. El controlador recibe el parámetro **id_contacto:HASH** desde la URL (GET) y verifica la integridad del HASH utilizando la palabra **CLAVE_SECRETA**.
    2. Si la firma es válida, extrae el id_contacto original, consulta la tabla **contactos** en Supabase y renderiza en la vista los campos: foto, nombre, email y telefono, junto con un enlace para volver a **lista_contactos**.

* **Flujo alternativo (Error)**:

    1. Si el HASH fue alterado o el registro no existe en la base de datos, el sistema muestra el mensaje "**Contacto no encontrado**" y un enlace para regresar a **lista_contactos**.

### RF06 - Insertar nuevo contacto (insertar_contacto)

* **Descripción**: Permite registrar un nuevo contacto en el sistema.

* **Flujo principal**:

    1. La vista muestra un formulario con los campos: nombre (type: text), email (type:email), telefono (type:tel) y foto (type:file), además de los botones "**Insertar**" y "**Cancelar**".
    2. Al presionar "**Insertar**", el controlador valida los datos, sube la imagen, la alamacena en **static/fotos/** (usando un **timestamp** por nombre del archivo), por último ejecuta la inserción en la tabla **contactos** de Supabase.
    3. El sistema muestra el mensaje "**Contacto insertado correctamente**" y proporciona un enlace para regresar a **lista_contactos**.

* **Flujo alternativo**:

    1. Si el usuario presiona "**Cancelar**", el sistema descarta el formulario y redirige inmediatamente a **lista_contactos**.

### RF07 - Actualizar contacto (actualizar_contacto)

* **Descripción**: Permite modificar los datos de un contacto existente.

* **Flujo principal**:

    1. El controlador recibe el parámetro **id_contacto:HASH** por URL(GET) y valida la integridad del HASH.
    2. Si es válido, consulta los datos actuales del contacto en Supabase y los muestra en un formulario con los campos editables (nombre, email, telefono, foto) y los botones "**Actualizar**" y "**Cancelar**".
    3. Al presionar "**Actualizar**", el controlador valida nuevamente el **id_contacto:HASH**, procesa los cambios (actualizando la foto solo si se cargó una nueva) y ejecuta la actualización en la tabla **contactos** de Supabase.
    4. El sistema muestra el mensaje "**Contacto actualizado correctamente**" junto con un enlace para regresar a **lista_contactos**.

* **Flujo alternativo**:

    1. Si el HASH es inválido o el contacto no existe, muestra el mensaje "**Contacto no encontrado**" junto con un enlace para regresar a **lista_contactos**.
    2. Si el usuario presiona "**Cancelar**", redirige a **lista_contactos** sin guardar cambios.

### RF08 - Borrar contacto (borrar_contacto)

* **Descripción**: Permite eliminar permanentemente un contacto existente previa visualización de sus datos.

* **Flujo principal**:

    1. El controlador recibe el parámetro **id_contacto:HASH** por URL (GET) y valida la integridad del HASH.
    2. Si es válido, consulta los datos actuales del contacto en Supabase y los muestra en una vista con los campos de solo lectura (foto, nombre, email, telefono) y los botones "**Borrar**" y "**Cancelar**".
    3. Al presionar "**Borrar**", el controlador valida nuevamente el **id_contacto:HASH**, elimina el archivo de imagen asociado en **static/fotos** (si existe) y ejecuta la eliminación del registro en la tabla **contactos** de Supabase.
    4. El sistema muestra el mensaje "**Contacto eliminado correctamente**" junto con un enlace para regresar a **lista_contactos**.

* **Flujo alternativo**:

    1. Si el HASH es inválido o el contacto no existe, muestra el mensaje "**Contacto no encontrado**", y un enlace a la página **lista_contactos**.
    2. Si el usuario presiona "**Cancelar**", redirige a lista_contactos sin borrar el registro.
