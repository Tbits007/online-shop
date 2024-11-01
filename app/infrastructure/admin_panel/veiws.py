from sqladmin import ModelView
from app.domain.users import Users
from app.domain.categories import Categories
from app.domain.products import Products
from app.domain.orders import Orders


class UsersAdmin(ModelView, model=Users):
    name = "User"
    name_plural = "Users"
    column_list = '__all__'


class CategoriesAdmin(ModelView, model=Categories):
    name = "Category"
    name_plural = "Categories"
    column_list = '__all__'


class ProductsAdmin(ModelView, model=Products):
    name = "Product"
    name_plural = "Products"
    column_list = '__all__'


class OrdersAdmin(ModelView, model=Orders):
    name = "Order"
    name_plural = "Orders"
    column_list = '__all__'