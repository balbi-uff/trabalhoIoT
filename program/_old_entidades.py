from requests import delete, get, post, put
import json
from config import debugger, URL_ORION, URL_CREATE_ENTITY, URL_GET_ALL_ENTITIES, URL_PUT_ENTITY, URL_PUT_BATCH


class Entidade:
    name = ""
    
    def create(self, entity_id):
        payload = {
            "id": entity_id, "type": self.name,
            "status":{"type":"Boolean", "value":"false"}
        }
        debugger(f"Creating {self.name}: " + entity_id)
        response = post(URL_CREATE_ENTITY, headers={"Content-Type": "application/json"}, json=payload)
        if(response.status_code == 400):
            debugger(f"Error creating {self.name}: " + response.text, "Error")
        elif(response.status_code == 201):
            debugger(f"{self.name} created: " + entity_id)
        
    def createMultiple(self, numeroDeEntidades):
        """
            Cria numeroDeEntidades Entidades. -> Implementação iterada: sem usar batch.
        """
        STANDART_ENTITY_ID = f"urn:ngsi-ld:{self.name}:"
        [self.create(STANDART_ENTITY_ID + str(id)) for id in range(numeroDeEntidades)]
        
    def getAll(self):
        entities = json.loads(get(URL_GET_ALL_ENTITIES).text)
        return list(filter(lambda e : e["type"] == self.name, entities))
        
    def deletarAll(self):
        for entidade in self.getAll():
            debugger("Deleting Entidade: " + entidade["id"])
            response = delete(URL_ORION + "/v2/entities/" + entidade["id"])
            if(response.status_code == 400):
                debugger("Error deleting " + str(entidade["id"]) + ":" + response.text, "Error")
            elif(response.status_code == 201):
                debugger(f"{self.name} deleted: " + entidade["id"])
        
    def batchAlterarStatus(self, status):
        entidades = self.getAll()
        for entidade in entidade:
            entidade["status"]["value"] = str(status).lower()
        
        payload = {
            "actionType": "update",
            "entities": entidades
        }
        
        response = post(URL_PUT_BATCH, headers={"Content-Type": "application/json"}, json=payload)
        if response.status_code != 204:
            debugger(f"Erro alterando status {self.name}: " + response.text, "Error")
        else:
            debugger(f"Status das {self.name} alterado!: " + str(status))
            
            
class Lampada(Entidade):
    def __init__(self):
        self.name = "Lampada"
        
class ArCondicionado(Entidade):
    def __init__(self):
        self.name = "ArCondicionado"

class SalaDeAula():
   
    name = "SalaDeAula"
    entity_id = "urn:ngsi-ld:SalaDeAula:1"
        
    def create(self):
        payload = {
            "id": self.entity_id, "type": self.name,
            "temperatura":{"type":"Number", "value":"20"},
            "status_atividade":{"type":"Boolean", "value":"false"}, # 0 (sem atividade) - 1 (pelo menos uma pessoa)
        }
        
        debugger(f"Creating {self.name}: " + self.entity_id)
        response = post(URL_CREATE_ENTITY, headers={"Content-Type": "application/json"}, json=payload)
        if(response.status_code == 400):
            debugger(f"Error creating {self.name}: " + response.text, "Error")
        elif(response.status_code == 201):
            debugger(f"{self.name} created: " + self.entity_id)
            
    def delete(self):
        response = delete(URL_ORION + "/v2/entities/" + self.entity_id)
        if(response.status_code == 400):
            debugger("Error deleting " + str(self.entity_id) + ":" + response.text, "Error")
        elif(response.status_code == 201):
            debugger(f"{self.name} deleted: " + self.entity_id)
            

a = ArCondicionado()
a.createMultiple(1)


