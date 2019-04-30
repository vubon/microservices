import os
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_NAME = 'transactions_service'


def load_config(path):
    with open(path, 'rt') as f:
        conf = yaml.safe_load(f)
    return conf


db_params = {
    'provider': 'postgres',
    'host': 'localhost',
    'database': 'service_1',
    'user': 'postgres',
    'password': 'postgres',
    'migration_dir': 'service_1/transactions/migrations'
}
