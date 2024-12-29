from openai import BaseModel
from pydantic import Field


class CodeConvertGenerateResponse(BaseModel):
    result: str = Field("변환된 코드")
