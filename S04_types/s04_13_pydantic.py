from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Ortiz Ordoñez'
    signup_ts: datetime| None = None
    friends: list[int] = []

# Desde el exterior podríamos recibir estos datos:
external_data = {
    'id' : 1001,
    'name' : "Otro Nombre",
    'signup_ts' : '2023-12-16 13:45',
    'friends' : [1002, 1003, 1004]
}

user = User(**external_data)
print(user)
print(user.id)
