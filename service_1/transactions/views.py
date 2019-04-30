import sys
import datetime
import json
import decimal
from asyncio_extras import threadpool
from aiohttp import web
from pony.orm import *
from .models import Transactions, create_transaction, User, db_session, test_create, db


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        elif isinstance(obj, datetime.datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


async def home_page(request):
    async with threadpool():
        with db_session:
            users = User.select()[:]
    return web.json_response(data={"success_code": "SC", "data": [user.to_dict() for user in users]},
                             status=200)


async def create_user(request):
    await test_create(await request.json())
    return web.json_response(data={"success_code": "UR201"}, status=201)


async def transactions(request):
    async with threadpool():
        with db_session:
            trans = [json.dumps(trn.to_dict(), cls=DecimalEncoder) for trn in Transactions.select()[:]]
    return web.json_response(
        data={
            "success_code": "TR200",
            "data": [json.loads(trn) for trn in trans],
        },
        status=200
    )


async def create_transaction_view(request):
    """
    :param request:
    :return:
    """
    # test(await request.json())
    await create_transaction(await request.json())

    return web.json_response(data={"succes_code": "TR201"}, status=201)
