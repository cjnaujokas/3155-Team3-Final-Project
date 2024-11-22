from . import orders, order_details, recipes, food_items, resources, reviews, complete_orders, users

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    food_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    complete_orders.Base.metadata.create_all(engine)
    users.Base.metadata.create_all(engine)
