
"""
    This module contains the Subscriptions class.
"""

"""
    Se Sala.status_atividade == True -> Ligar luzes
"""
payload_1 = {
  "description": "Se sala statusAtividade == True -> Ligar luzes",
  "subject": {
    "entities": [{"idPattern": ".*", "type": "SalaDeAula"}],
    "condition": {
      "attrs": [ "status_atividade" ],
      "expression" : {
          "q": "status_atividade==true"
      }
    }
  },
  "notification": {
    "http": {
      "url": "endpoint_ligar_ar_condicionado"
    }
  }
}
"""
    Se Sala.status_atividade == False -> Desligar luzes
"""

payload_2 = {
  "description": "Se Sala.status_atividade == False -> Ligar luzes",
  "subject": {
    "entities": [{"idPattern": ".*", "type": "SalaDeAula"}],
    "condition": {
      "attrs": [ "status_atividade" ],
      "expression" : {
          "q": "status_atividade==false"
      }
    }
  },
  "notification": {
    "http": {
      "url": "endpoint_desligar_ar_condicionado"
    }
  }
}


"""
    Se Sala.temperatura > 25 -> Ligar ar condicionado
"""

"""
    Se Sala.temperatura < 18 -> Desligar ar condicionado
"""
