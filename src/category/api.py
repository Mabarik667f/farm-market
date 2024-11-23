from ninja_extra import ControllerBase, api_controller, route
from category.schemas import CategoryOut, CreateCategory
from category import crud

@api_controller("/categories", tags=["categories"], permissions=[])
class CategoryAPI(ControllerBase):
    @route.post('/', response={201: CategoryOut})
    def create_category(self, payload: CreateCategory):
        return crud.create_category(payload)

    @route.get('/{category_id}', response={200: CategoryOut})
    def get_category(self, category_id: int):
        return crud.get_category(category_id)

    @route.get("/", response={200: list[CategoryOut]})
    def list_categories(self):
        return crud.list_categories()

    @route.delete("/{category_id}", response={204: None})
    def del_category(self, category_id: int):
        crud.del_category(category_id)
