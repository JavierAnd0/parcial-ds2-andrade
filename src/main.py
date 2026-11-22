import pymongo
from pymongo import MongoClient

from modelo import CampanaPruebas

uri = ("mongodb://admin:123456@localhost:27017/?authSource=admin")
client = MongoClient(uri)

try:
    database = client.get_database("matriculapp")
    semanas = database.get_collection("semana")

    results = semanas.find({}).sort("numeroSemana", pymongo.ASCENDING).limit(8)

    defectos = []
    for semana in results:
        defectos.append(semana["numeroDefectos"])

    client.close()
except Exception as e:
    raise Exception("Unable to find the documents due to the following error: ", e)

campana =  CampanaPruebas(defectos)
campana.ajustar()

print("Defectos:", defectos)
print("Acumulados:", campana.hallados)
print("Defectos totales:", round(campana.a))
print("Tasa b:", round(campana.b, 4))
print("Defectos restantes", round(campana.restantes()))
print("Semana donde llega al 95%", round(campana.semana_95(),1))

campana.graficar()

