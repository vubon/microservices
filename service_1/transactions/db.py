from pony.orm import *

db = Database()


async def init_db(db_config):
    db.bind(provider='postgres', user=db_config['username'], password=db_config['password'],
            host=db_config['host'], database=db_config['database'] )
    db.generate_mapping(create_tables=True)
    sql_debug(True)
