import os
from supabase import create_client, Client
from dotenv import load_dotenv
import hashlib
import hmac

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )
            self.SECRET_KEY = b"hola"
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def generar_hash(self,id: int) -> str:
        try:
            """Genera un hash único a partir del ID."""
            mensaje = str(id).encode("utf-8")
            firma =  hmac.new(self.SECRET_KEY, mensaje, hashlib.sha256).hexdigest()
            return f"{id}:{firma}"
        except Exception as error:
            print(f"ERROR 106: {error.args[0]}")
            return ""


    def validar_hash(self,hash_a_validar: str) -> int:
        try:
            # Separa el id y la firma
            id_str, sep, _ = hash_a_validar.partition(":")
            resultado_id = -1

            # Solo calculamos el hash si la estructura básica es válida
            if sep and id_str.isdigit():
                token_esperado = self.generar_hash(int(id_str))
                if hmac.compare_digest(token_esperado, hash_a_validar):
                    resultado_id = int(id_str)
                else:
                    resultado_id = -1
            else:
                resultado_id = -1

            return resultado_id
        except Exception as error:
            print(f"ERROR 107: {error.args[0]}")
            return -1

    def obtenerContactos(self):
        try:
            # SELECT * FROM contactos;
            response = self.supabase.table("contactos").select("*").execute()
            for registro in response.data:
                registro["id_contacto"] = self.generar_hash(registro["id_contacto"]) # type: ignore
            return response.data
        except Exception as error:
            print(f"ERROR 101: {error.args[0]}")

    def buscarContacto(self,id_contacto:str):
        try:
            id = self.validar_hash(id_contacto)
            # SELECT * FROM contactos WHERE id_contacto = ?;
            response = self.supabase.table("contactos").select("*").eq("id_contacto",id).execute()
            return response.data
        except Exception as error:
            print(f"ERROR 102: {error.args[0]}")

    def insertarContacto(self,nombre:str,email:str,telefono:str):
        try:
            # INSERT INTO contactos(nombre,email,telefono) VALUES(?,?,?);
            data = {
                "nombre":nombre,
                "email":email,
                "telefono":telefono
            }
            response = self.supabase.table("contactos").insert(data).execute()
            return response.data
        except Exception as error:
            print(f"ERROR 103: {error.args[0]}")

    def borrarContacto(self,id_contacto:str):
        try:
            id = self.validar_hash(id_contacto)
            # DELETE * FROM contactos WHERE id_contacto = ?;
            response = self.supabase.table("contactos").delete().eq("id_contacto",id).execute()
            return response.data
        except Exception as error:
            print(f"ERROR 104: {error.args[0]}")

    def actualizarContacto(self,id_contacto:str,nombre:str,email:str,telefono:str):
        try:
            id = self.validar_hash(id_contacto)
            # UPDATE SET nombre=?, email=?, telefono=? FROM contactos WHERE id_contacto=?;
            data = {
                "nombre":nombre,
                "email":email,
                "telefono":telefono
            }
            response = self.supabase.table("contactos").update(data).eq("id_contacto",id).execute()
            return response.data
        except Exception as error:
            print(f"ERROR 105: {error.args[0]}")


if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(2))
    print(model_contactos.insertarContacto("Carthoris","carthoris@email","333333"))
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.borrarContacto(4))
    #print(model_contactos.actualizarContacto(5,"Juan","juan@email","8888888"))
