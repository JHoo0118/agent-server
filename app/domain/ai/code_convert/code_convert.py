from pydantic import Field

from dataclasses import asdict, dataclass
from app.adapter.inbound.web.base_schema import BaseSchema
from typing import Final


@dataclass
class CodeConvert(BaseSchema):
    code: str = Field()
    code_type: str = Field()
    target_code_type: str = Field()

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def generate_code_convert(
        cls,
        code: "CodeConvert.Code",
        code_type: "CodeConvert.CodeType",
        target_code_type: "CodeConvert.TargetCodeType",
    ) -> "CodeConvert":
        return cls.model_construct(
            code=code.code,
            code_type=code_type.code_type,
            target_code_type=target_code_type.target_code_type,
        )

    @dataclass(frozen=True)
    class Code:
        code: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "code", value)

    @dataclass(frozen=True)
    class CodeType:
        code_type: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "code_type", value)

    @dataclass(frozen=True)
    class TargetCodeType:
        target_code_type: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "target_code_type", value)
