from openai import BaseModel
from pydantic import Field


class DiagramErdGenerateResponse(BaseModel):
    image: str = Field("생성된 ERD 이미지")
