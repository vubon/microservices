import asyncio
from aiohttp import web

# database connection
from service_1.transactions.db import init_db

# Route setup
from service_1.transactions.routes import setup_routes

from service_1.transactions.settings import load_config, BASE_DIR


async def init_app(config):
    """
    :param: config
    :return:
    """
    # setup main application
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    # Database init
    await init_db(config['postgres'])

    # setup routes
    setup_routes(app)

    return app


def main(config):
    """
    :param: config
    :return:
    """
    # config = load_config()
    app = init_app(config)
    web.run_app(app, port=config['port'], host=config['host'])


if __name__ == '__main__':
    # collect configuration
    config_data = load_config(BASE_DIR + '/config/config.yml')
    main(config_data)
