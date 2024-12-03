from . import orders, order_details, reviews, users, complete_orders, revenue, resources, promo_codes


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(reviews.router)
    app.include_router(users.router)
    app.include_router(complete_orders.router)
    app.include_router(revenue.router)
    app.include_router(resources.router)
    app.include_router(promo_codes.router)
