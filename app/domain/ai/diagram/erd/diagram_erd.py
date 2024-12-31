from dataclasses import asdict, dataclass
from typing import Final

from pydantic import Field

from app.adapter.inbound.web.base_schema import BaseSchema


@dataclass
class DiagramErd(BaseSchema):
    query: str = Field()

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def generate_diagram_erd(
        cls,
        query: "DiagramErd.Query",
    ) -> "DiagramErd":
        return cls.model_construct(
            query=query.query,
        )

    @dataclass(frozen=True)
    class Query:
        query: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "query", value)
