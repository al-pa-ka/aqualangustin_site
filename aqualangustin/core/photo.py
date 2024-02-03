from io import BytesIO
from typing import Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PhotoData:
    photo: BytesIO
    filename: Optional[str] = None
    ...

class Photo(ABC):
    @abstractmethod
    def get_serialized_data(self) -> dict: ...

