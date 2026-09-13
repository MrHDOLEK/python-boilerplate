from typing import Any

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: dict[str, str]


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> User:
        return cls(**data)
