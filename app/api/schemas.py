from pydantic import BaseModel, ConfigDict, Field


class Item(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=120)
    value: int


class ItemList(BaseModel):
    data: list[Item]
    total: int = Field(ge=0)
    offset: int = Field(ge=0)
    limit: int = Field(gt=0)
    timestamp: str


class ItemEnvelope(BaseModel):
    item: Item
    timestamp: str


class ServiceStatus(BaseModel):
    status: str
    service: str
    version: str
    environment: str
