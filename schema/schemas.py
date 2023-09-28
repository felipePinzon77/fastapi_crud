def individual_serial(todo) -> dict:
    return{
        "id": str(todo["_id"]),
        "nombre": todo["nombre"],
        "autor": todo["autor"],
        "editorial": todo["editorial"],
        "edicion": float(todo["edicion"]),
        "categoria": todo["categoria"],
        "precio": float(todo["precio"])

    }

def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]