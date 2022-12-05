from dataclasses import dataclass


@dataclass()
class Point:
    id: str
    relations: dict
