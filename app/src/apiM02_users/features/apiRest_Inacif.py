
from zeep import Client
from ..models import Ubicacion
import json
from decouple import config

class actualizarUbicaciones:
    def actualizar():
        client = Client(config('URL_API_INACIF')+'WebServiceRecursos.asmx?WSDL')
        result = json.loads(client.service.CargarUbicacion())

        i = 0
        for k, v in result:
            u2 = Ubicacion(ubi_codigo=result[i][k], nombre=result[i][v])
            u2.save()
            i = i+1

        print("listo")
        return "listo"
