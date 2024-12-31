import json

from app.adapter.inbound.web.base_schema import BaseSchema


class DiagramErdGenerateRequest(BaseSchema):
    query: str

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
