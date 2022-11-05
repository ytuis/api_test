from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    id: str
    title: str
    description: Union[str, None] = None
