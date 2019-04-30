import asyncio
from aiohttp import web

# database connection
from service_1.transactions.db import init_db

# Route setup
from service_1.transactions.routes import setup_routes


# from service_1.transactions.settings import load_config


async def init_app():
    """
    :return:
    """
    # setup main application
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    # Database init
    await init_db()

    # setup routes
    setup_routes(app)

    return app


def main():
    """
    :return:
    """
    # config = load_config()
    app = init_app()
    web.run_app(app, port=8000)


if __name__ == '__main__':
    main()
