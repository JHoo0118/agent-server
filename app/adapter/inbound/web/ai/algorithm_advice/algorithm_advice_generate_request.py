import json
from typing import List

from pydantic import Field

from app.adapter.inbound.web.ai.ai_model import ChatModel
from app.adapter.inbound.web.base_schema import BaseSchema


class AlgorithmAdviceGenerateRequest(BaseSchema):
    messages: List[ChatModel] = Field(...)
    lang: str = Field(...)

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
