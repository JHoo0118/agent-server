from pydantic import Field

from app.adapter.inbound.web.base_schema import BaseSchema


class CodeConvertGenerateRequest(BaseSchema):
    code: str = Field()
    code_type: str = Field()
    target_code_type: str = Field()
