from dataclasses import dataclass


@dataclass
class Dog:
    """Class for representing a kanine."""

    name: str
    age: int
    speed: float
    bark_pitch: float

    def bark_pitch_when_sad(self) -> float:
        return self.bark_pitch * (self.age / 10)


dog_a = Dog(name="Rex", age=5, speed=10.2, bark_pitch=4)


def test_dog_a_pitch_when_happy():
    assert dog_a.bark_pitch_when_sad() == 2.0


class DogNon:
    """Class for representing a kanine."""

    def __init__(self, name, age, speed, bark_pitch):
        self.name: str = name
        self.age: int = age
        self.speed: float = speed
        self.bark_pitch: float = bark_pitch

    def bark_pitch_when_sad(self) -> float:
        return self.bark_pitch * (self.age / 10)


dog_b = DogNon(name="Rex", age=5, speed=10.2, bark_pitch=4)
