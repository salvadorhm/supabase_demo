import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        try:
            # SELECT * FROM contactos;
            response = self.supabase.table("contactos").select("*").execute()
            return response.data
        except Exception as error:
            print(f"ERROR 101: {error.args[0]}")

    def buscarContacto(self,id_contacto:int):
        try:
            # SELECT * FROM contactos WHERE id_contacto = ?;
            response = self.supabase.table("contactos").select("*").eq("id_contacto",id_contacto).execute()
            return response.data
        except Exception as error:
            print(f"ERROR 102: {error.args[0]}")


if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(15))
