from . import orders, order_details, reviews, users, complete_orders, revenue


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(reviews.router)
    app.include_router(users.router)
    app.include_router(complete_orders.router)
    app.include_router(revenue.router)
