from typing import Dict, List, Union

from pydantic import BaseModel


class ChatModel(BaseModel):
    role: str
    content: Union[str, List[Union[str, Dict]]]
