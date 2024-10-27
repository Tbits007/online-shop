from pydantic import BaseModel


class CategoryCreateSchema(BaseModel):
    name: str
    description: str


class CategoryUpdateSchema(BaseModel):
    name: str
    description: str


class CategoryResponseSchema(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True