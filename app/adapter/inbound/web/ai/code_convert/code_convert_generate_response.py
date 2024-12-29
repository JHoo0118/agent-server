from pydantic import Field
from openai import BaseModel


class CodeConvertGenerateResponse(BaseModel):
    result: str = Field("변환된 코드")
