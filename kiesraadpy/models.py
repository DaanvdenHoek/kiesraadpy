from typing import Any
import datetime
from enum import Enum
from pydantic import BaseModel, field_validator, Field
from kiesraadpy.utils import parse_dutch_date_string


class ElectionType(Enum):
    TWEEDE_KAMER = ('Tweede Kamer', 'TK')
    EUROPEES_PARLEMENT = ('Europees Parlement', 'EP')

    @property
    def long(self):
        return self.value[0]
    
    @property
    def short(self):
        return self.value[1]

    @classmethod
    def from_long(cls, value: str) -> 'ElectionType':
        for type in cls:
            if type.long == value:
                return type
        raise ValueError(f'No electionType with long name {value} found')

    @classmethod
    def from_short(cls, value: str) -> 'ElectionType':
        for type in cls:
            if type.short == value:
                return type
        raise ValueError(f'No electionType with long name {value} found')
    

class ElectionIndexResult(BaseModel):
    date: datetime.date = Field(alias='datum')
    type: ElectionType = Field(alias='verkiezingsnaam')
    vote_count: int | None = Field(alias='value')

    @field_validator('vote_count', mode='before')
    @classmethod
    def parse_vote_count(cls, v: str) -> int:
        v = v.replace('.', '')
        return int(v) if v.isnumeric() else None
    
    @field_validator('date', mode='before')
    @classmethod
    def parse_date(cls, v: str) -> datetime.date:
        return parse_dutch_date_string(v)