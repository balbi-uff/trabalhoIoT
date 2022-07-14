from requests import delete, get, post, put, patch
from config import debugger, URL_ORION, URL_CREATE_ENTITY, URL_GET_ALL_ENTITIES, URL_PUT_ENTITY, URL_PUT_BATCH

############################# GLOBALS #####################################
# Urls raízes
URL_IOTA = "http://localhost:7896"
URL_TUTORIAL = "http://localhost:3001"
URL_NGSI = "http://localhost:4041"

# outras Urls
URL_PROVIDE_SERVICE_GROUP = URL_NGSI + "/iot/services"
URL_PROVIDE_SENSOR = URL_NGSI + "/iot/devices"
URL_DISPOSITIVOS = URL_PROVIDE_SENSOR

# ACs
URL_ENDPOINT_AC_1 = URL_TUTORIAL + "/iot/AC001"
URL_ENDPOINT_AC_2 = URL_TUTORIAL + "/iot/AC002"

# lampadas
URL_ENDPOINT_LAMP_1 = URL_TUTORIAL + "/iot/LAMP001"
URL_ENDPOINT_LAMP_2 = URL_TUTORIAL + "/iot/LAMP002"
URL_ENDPOINT_LAMP_3 = URL_TUTORIAL + "/iot/LAMP003"
URL_ENDPOINT_LAMP_4 = URL_TUTORIAL + "/iot/LAMP004"

# headers

HEADERS_SENSOR = {
    "Content-Type": "application/json",
    "fiware-service": "openiot",
    "fiware-servicepath": "/"
}
HEADERS_SERVICE_GROUP = HEADERS_SENSOR
HEADERS_DISPOSIVOS = HEADERS_SENSOR

# vars globais 

id_sala_de_aula = "urn:ngsi-ld:SalaDeAula:001"	
group_key = "4jggokgpepnvsb2uv4s40d59ov"



################################## MAIN #####################################

""" 
    setup SalaDeAula
"""
def setupSaladeAula():
    payload = {
                "id": id_sala_de_aula, "type": "SalaDeAula",
            }
            
    debugger(f"Creating {id_sala_de_aula}: " + id_sala_de_aula)
    response = post(URL_CREATE_ENTITY, headers={"Content-Type": "application/json"}, json=payload)
    if(response.status_code == 400):
        debugger(f"Error creating {id_sala_de_aula}: " + response.text, "Error")
    elif(response.status_code == 201):
        debugger(f"{id_sala_de_aula} created: " + id_sala_de_aula)
   
          
"""
    setup Service Group
"""
def setupServiceGroup():
    payload = {
        "services": [{
            "apikey":      group_key,
            "cbroker":     "http://orion:1026",
            "entity_type": "Thing",
            "resource":    "/iot/json"
        }]       
    }
    response = post(URL_PROVIDE_SERVICE_GROUP, headers=HEADERS_SERVICE_GROUP, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando Service Group: " + response.text, "Error")
    else:
        debugger(f"Service Group criado: " + response.text)

"""
    setup Sensor de Movimento
"""
def setupSensorMovimento():
    payload = {
        "devices": [
            {
                "device_id":   "motion111",
                "entity_name": "urn:ngsi-ld:Motion:111",
                "entity_type": "Motion",
                "attributes": [
                { "object_id": "mov", "name": "status_movimento", "type": "Boolean" }
                ],
                "static_attributes": [
                { "name":"relacaoSalaDeAula", "type": "Relationship", "value": id_sala_de_aula}
                ]
            }
        ]
    }
    
    response = post(URL_PROVIDE_SENSOR, headers=HEADERS_SENSOR, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando Sensor de Movimento: " + response.text, "Error")
    else:
        debugger(f"Sensor de Movimento instanciado! " + response.text)
        
"""
 setup Sensor de Temperatura
"""
def setupSensorTemperatura():
    payload = {
        "devices": [
            {
                "device_id":   "temperature001",
                "entity_name": "urn:ngsi-ld:Temperature:001",
                "entity_type": "Temperature",
                "attributes": [
                { "object_id": "temp", "name": "temperatura", "type": "Number" }
                ],
                "static_attributes": [
                { "name":"relacaoSalaDeAula", "type": "Relationship", "value": id_sala_de_aula}
                ]
            }
        ]
    }
    
    response = post(URL_PROVIDE_SENSOR, headers=HEADERS_SENSOR, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando Sensor de Temperatura: " + response.text, "Error")
    else:
        debugger(f"Sensor de Temperatura instanciado! " + response.text)

"""
    Alterar estado Sensor de Movimento
"""

def AlterarEstadoSensorDeMovimento(estado_novo="true"):
    URL_SIMULATE_MOV = URL_IOTA + "/iot/json/?k="+ group_key + "&i=motion111"
    HEADERS_SIMULATE_MOV = {"Content-Type": "application/json"}
    payload = {
        "mov" : estado_novo
    }
    
    response = post(URL_SIMULATE_MOV, headers=HEADERS_SIMULATE_MOV, json=payload)
    if(response.status_code != 200):
        debugger(f"Erro alterando estado Sensor de Movimento: " + response.text, "Error")
    else:
        debugger(f"Estado Sensor de Movimento alterado para: {estado_novo}" + response.text)


"""
setup Arcondicionado 1
"""
def setupArcondicionado1():
    payload = {
        "devices": [
            {
            "device_id": "AC001",
            "entity_name": "urn:ngsi-ld:AC:001",
            "entity_type": "AC",
            "transport": "HTTP",
            "endpoint": URL_ENDPOINT_AC_1,
            "commands": [
                { "name": "turn_on", "type": "command" },
                { "name": "turn_off", "type": "command" }
            ],
            "static_attributes": [
                {"name":"refStore", "type": "Relationship","value": id_sala_de_aula}
            ]
            }
        ]
    }
    
    response = post(URL_DISPOSITIVOS, headers=HEADERS_DISPOSIVOS, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando ArCondicionado 1: " + response.text, "Error")
    else:
        debugger(f"ArCondicionado 1 instanciado! " + response.text)
    
"""
setup Arcondicionado 2
"""
def setupArcondicionado2():
    payload = {
        "devices": [
            {
            "device_id": "AC002",
            "entity_name": "urn:ngsi-ld:AC:002",
            "entity_type": "AC",
            "transport": "HTTP",
            "endpoint": URL_ENDPOINT_AC_2,
            "commands": [
                { "name": "turn_on", "type": "command" },
                { "name": "turn_off", "type": "command" }
            ],
            "static_attributes": [
                {"name":"refStore", "type": "Relationship","value": id_sala_de_aula}
            ]
            }
        ]
    }
    
    response = post(URL_DISPOSITIVOS, headers=HEADERS_DISPOSIVOS, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando ArCondicionado 2: " + response.text, "Error")
    else:
        debugger(f"ArCondicionado 2 instanciado! " + response.text)

"""
setup Lampada 1
"""
def setupLampada1():
    payload = {
        "devices": [
            {
            "device_id": "Lamp001",
            "entity_name": "urn:ngsi-ld:Lamp:001",
            "entity_type": "Lamp",
            "transport": "HTTP",
            "endpoint": URL_ENDPOINT_LAMP_1,
            "commands": [
                { "name": "turn_on", "type": "command" },
                { "name": "turn_off", "type": "command" }
            ],
            "attributes": [
                {"object_id": "s", "name": "state", "type":"Boolean"}
            ],
            "static_attributes": [
                {"name":"refStore", "type": "Relationship","value": id_sala_de_aula}
            ]
            }
        ]
    }
    
    response = post(URL_DISPOSITIVOS, headers=HEADERS_DISPOSIVOS, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando Lampada 1: " + response.text, "Error")
    else:
        debugger(f"Lampada 1 instanciado! " + response.text)

"""
setup Lampada 2
"""
def setupLampada2():
    payload = {
        "devices": [
            {
            "device_id": "Lamp002",
            "entity_name": "urn:ngsi-ld:Lamp:002",
            "entity_type": "Lamp",
            "transport": "HTTP",
            "endpoint": URL_ENDPOINT_LAMP_2,
            "commands": [
                { "name": "turn_on", "type": "command" },
                { "name": "turn_off", "type": "command" }
            ],
            "attributes": [
                {"object_id": "s", "name": "state", "type":"Boolean"}
            ],
            "static_attributes": [
                {"name":"refStore", "type": "Relationship","value": id_sala_de_aula}
            ]
            }
        ]
    }
    
    response = post(URL_DISPOSITIVOS, headers=HEADERS_DISPOSIVOS, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando Lampada 2: " + response.text, "Error")
    else:
        debugger(f"Lampada 2 instanciado! " + response.text)

"""
setup Lampada 3
"""
def setupLampada3():
    payload = {
        "devices": [
            {
            "device_id": "Lamp003",
            "entity_name": "urn:ngsi-ld:Lamp:003",
            "entity_type": "Lamp",
            "transport": "HTTP",
            "endpoint": URL_ENDPOINT_LAMP_3,
            "commands": [
                { "name": "turn_on", "type": "command" },
                { "name": "turn_off", "type": "command" }
            ],
            "attributes": [
                {"object_id": "s", "name": "state", "type":"Boolean"}
            ],
            "static_attributes": [
                {"name":"refStore", "type": "Relationship","value": id_sala_de_aula}
            ]
            }
        ]
    }
    
    response = post(URL_DISPOSITIVOS, headers=HEADERS_DISPOSIVOS, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando Lampada 3: " + response.text, "Error")
    else:
        debugger(f"Lampada 3 instanciado! " + response.text)

"""
setup Lampada 4
"""
def setupLampada4():
    payload = {
        "devices": [
            {
            "device_id": "Lamp004",
            "entity_name": "urn:ngsi-ld:Lamp:004",
            "entity_type": "Lamp",
            "transport": "HTTP",
            "endpoint": URL_ENDPOINT_LAMP_4,
            "commands": [
                { "name": "turn_on", "type": "command" },
                { "name": "turn_off", "type": "command" }
            ],
            "attributes": [
                {"object_id": "s", "name": "state", "type":"Boolean"}
            ],
            "static_attributes": [
                {"name":"refStore", "type": "Relationship","value": id_sala_de_aula}
            ]
            }
        ]
    }
    
    response = post(URL_DISPOSITIVOS, headers=HEADERS_DISPOSIVOS, json=payload)
    if response.status_code != 201:
        debugger(f"Erro criando Lampada 4: " + response.text, "Error")
    else:
        debugger(f"Lampada 4 instanciado! " + response.text)


"""
    Ligar e Desligar - Lampada 1
"""
def ligarLampada1():
    payload = {
        "turn_on": {
            "type" : "command",
            "value" : ""
        }
    }
       
    response = patch(URL_ORION + "/v2/entities/urn:ngsi-ld:Lamp:001/attrs", headers=HEADERS_DISPOSIVOS, json=payload)
    if response.status_code != 204:
        debugger(f"Erro ligando Lampada 1: " + response.text, "Error")
    else:
        debugger(f"Lampada 1 ligada! " + response.text)
        
ligarLampada1()
#def desligarLampada1():