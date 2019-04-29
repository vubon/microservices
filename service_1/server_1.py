import json
from decimal import Decimal
import asyncio
from datetime import datetime

from asyncio_extras import threadpool
from aiohttp import web
from pony.orm import *
from pony.orm.serialization import to_dict

db = Database()


class Transactions(db.Entity):
    id = PrimaryKey(int, auto=True)
    agent_phone = Required(str)
    agent_device = Required(str)
    amount = Required(Decimal)
    tran_type = Required(str)
    tran_reference = Required(str)
    from_account = Required(str)
    to_account = Required(str)
    auth_method = Optional(str)
    tran_status = Required(str)
    details = Optional(str)
    spp_name = Required(str)
    created_at = Required(datetime)
    updated_at = Optional(datetime)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)


db.bind('sqlite', './test.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


async def create_transaction(data):
    """
    :param data:
    :return:
    """
    async with threadpool():
        with db_session:
            for item in data:
                Transactions(
                    agent_phone=item['agent_phone'],
                    agent_device=item['agent_device'],
                    amount=item['amount'],
                    tran_type=item['tran_type'],
                    tran_reference=item['tran_reference'],
                    from_account=item['from_account'],
                    to_account=item['to_account'],
                    tran_status=item['tran_status'],
                    details=item['details'],
                    spp_name=item['spp_name'],
                    created_at=datetime.now(),
                )


def test(data):
    """
    :param data:
    :return:
    """
    print(data)
    for item in data:
        with db_session:
            user_obj = User(
                name=item['name']
            )
            print(user_obj)


async def home_page(request):
    async with threadpool():
        with db_session:
            # user = User.select_by_sql('SELECT * FROM User')
            # users = select(user for user in User)[:]
            users = User.select()[:]
    return web.json_response(data={"success_code": "SC", "data": [user.to_dict() for user in users]}, status=200)


async def transaction_data(request):
    """
    :param request:
    :return:
    """
    # test(await request.json())
    await create_transaction(await request.json())

    return web.json_response(data={"succes_code": "TR201"}, status=201)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', home_page)
    app.router.add_route('POST', '/create-transaction/', transaction_data)
    web.run_app(app, port=8000)
