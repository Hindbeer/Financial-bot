from dataclasses import dataclass
from os import environ


@dataclass
class Config:
    TELEGRAM_TOKEN: str = environ['TELEGRAM_TOKEN']
