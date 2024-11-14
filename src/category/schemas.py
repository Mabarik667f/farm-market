from ninja import Schema

class Category(Schema):
    name: str


class CreateCategory(Category):
    pass


class CategoryOut(Category):
    id: int
