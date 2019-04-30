# class MyEntity(db.Entity):
#     attr1 = Required(int)  # Usual INT column
#     attr2 = Required(long)  # BIGINT column
#     attr3 = Required(int, sql_type='BIGINT')  # alternative way

# attr1 = Required(int, size=8)  # 8 bit - TINYINT in MySQL
# attr2 = Required(int, size=16)  # 16 bit - SMALLINT in MySQL
# attr3 = Required(int, size=24)  # 24 bit - MEDIUMINT in MySQL
# attr4 = Required(int, size=32)  # 32 bit - INTEGER in MySQL
# attr5 = Required(int, size=64)  # 64 bit - BIGINT in MySQL
from decimal import Decimal
from datetime import datetime
from asyncio_extras import threadpool
from pony.orm import *
from service_1.transactions.db import db


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


async  def test_create(data):
    """
    :param data:
    :return:
    """
    print(data)
    async with threadpool():
        with db_session:
            for item in data:
                with db_session:
                     User(
                        name=item['name']
                    )
