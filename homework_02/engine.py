"""
create dataclass `Engine`
"""
from dataclasses import dataclass, field

@dataclass
class Engine:
    """ defaults """
    volume: int
    pistons: int


    def __init__(self, volume, pistons):

        self.volume = volume
        self.pistons = pistons
