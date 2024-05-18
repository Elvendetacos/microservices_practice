from typing import Optional

from pydantic import BaseModel


class Base_response(BaseModel):
    message: str
    data: Optional[list]
