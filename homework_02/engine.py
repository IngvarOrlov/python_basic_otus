"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: int | float
    pistons: int
