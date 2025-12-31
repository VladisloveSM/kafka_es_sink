import json

def process_message(value: bytes) -> dict:
    data = json.loads(value.decode("utf-8"))
    
    # тут можно:
    # - нормализовать поля
    # - переименовывать ключи
    # - валидировать
    return data
