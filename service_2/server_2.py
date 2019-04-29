import asyncio
from asyncio_extras import threadpool
from aiohttp import web
from pony.orm import *

db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)


db.bind('sqlite', './test.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
with db_session:
    u1 = User(name='One')
    u2 = User(name='Two')
    u3 = User(name='Three')

data = [
    {
        "agent_phone": "01737388296",
        "amount": "3000.0000",
        "agent_device": "Bscks123kshfjksfj",
        "tran_type": "Deposit",
        "tran_reference": "BVd14242",
        "from_account": "0006-000001254874",
        "to_account": "0002-0125478014",
        "auth_method": "",
        "tran_status": "Requested",
        "details": "Test",
        "spp_name": "Jamuna Bank"
    },
    {
        "agent_phone": "01737388296",
        "agent_device": "Bscks123kshfjksfj",
        "tran_type": "Deposit",
        "amount": "3000.0000",
        "tran_reference": "BVd14242",
        "from_account": "0006-000001254874",
        "to_account": "0002-0125478014",
        "auth_method": "",
        "tran_status": "Requested",
        "details": "Test",
        "spp_name": "Jamuna Bank"
    },
    {
        "agent_phone": "01737388296",
        "amount": "3000.0000",
        "agent_device": "Bscks123kshfjksfj",
        "tran_type": "Deposit",
        "tran_reference": "BVd14242",
        "from_account": "0006-000001254874",
        "to_account": "0002-0125478014",
        "auth_method": "",
        "tran_status": "Requested",
        "details": "Test",
        "spp_name": "Jamuna Bank"
    },
    {
        "agent_phone": "01737388296",
        "amount": "3000.0000",
        "agent_device": "Bscks123kshfjksfj",
        "tran_type": "Deposit",
        "tran_reference": "BVd14242",
        "from_account": "0006-000001254874",
        "to_account": "0002-0125478014",
        "auth_method": "",
        "tran_status": "Requested",
        "details": "Test",
        "spp_name": "Jamuna Bank"
    }
]


async def sample_handler(request):
    # id = int(request.match_info.get('id', 0))
    async with threadpool():
        with db_session:
            user = User.get(id=0)
            name = user.name if user else 'Anonymous'
    return web.Response(text="Hello, %s" % name)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', sample_handler)
    app.router.add_route('GET', '/{id}', sample_handler)
    web.run_app(app, port=9000)
