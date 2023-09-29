def individual_serial(todo) -> dict:
    return{
        "id": str(todo["_id"]),
        "nombre": todo["nombre"],
        "numero": int(todo["numero"])
    }

def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]