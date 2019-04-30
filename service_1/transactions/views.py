import json
from asyncio_extras import threadpool
from aiohttp import web
from .models import Transactions, create_transaction, User, db_session


async def home_page(request):
    async with threadpool():
        with db_session:
            # user = User.select_by_sql('SELECT * FROM User')
            # users = select(user for user in User)[:]
            users = User.select()[:]
    return web.json_response(data={"success_code": "SC", "data": [json.dumps(user.to_dict()) for user in users]},
                             status=200)


async def transactions(request):
    async with threadpool():
        with db_session:
            trans = Transactions.select()[:]
    return web.json_response(data={"success_code": "TR200", "data": [trn.to_dict() for trn in trans]}, status=200)


async def create_transaction_view(request):
    """
    :param request:
    :return:
    """
    # test(await request.json())
    await create_transaction(await request.json())

    return web.json_response(data={"succes_code": "TR201"}, status=201)
