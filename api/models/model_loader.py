from . import orders, order_details, recipes, food_items, resources, reviews, revenue, promo_codes

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    food_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    revenue.Base.metadata.create_all(engine)
    promo_codes.Base.metadata.create_all(engine)
