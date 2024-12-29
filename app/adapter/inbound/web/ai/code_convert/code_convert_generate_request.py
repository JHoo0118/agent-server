from pydantic import BaseModel, Field


class CodeConvertGenerateRequest(BaseModel):
    code: str = Field()
    code_type: str = Field()
    target_code_type: str = Field()
