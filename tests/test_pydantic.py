from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str
    age: int
    gender: str = Field(default="male" if 0 else "female")

def test_pydantic():
    person = Person(name="John", age=30)
    assert person.name == "John"
    assert person.age == 30
    assert person.gender == "female"