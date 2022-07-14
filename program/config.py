
URL_ORION = "http://localhost:1026"
URL_CREATE_ENTITY = URL_ORION + "/v2/entities"
URL_GET_ALL_ENTITIES = URL_ORION + "/v2/entities"
URL_PUT_ENTITY = URL_ORION + "/v2/entities/"
URL_PUT_BATCH = URL_ORION + "/v2/op/update"


def debugger(message, status="Info"):
    if status == "Info":
        print("[Info] >> " + message)
    elif status == "Error":
        print("!!! [Error] >> " + message)
    elif status == "Warning":
        print("! [Warning] >> " + message)
    else:
        print("[DebuggerError] !>> INVALID STATUS! @ debug.py")
    