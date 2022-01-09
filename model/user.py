import random
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Gender(str, Enum):
    male = "Male"
    female = "Female"


class User(BaseModel):
    id: Optional[int] = random.randrange(0, 10)
    name: str
    gender: Gender
    latitude: Optional[float]
    longitude: Optional[float]

