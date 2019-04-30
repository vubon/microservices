from pony.orm import *

db = Database()


async def init_db():
    db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='service_1')
    db.generate_mapping(create_tables=True)
    sql_debug(True)
