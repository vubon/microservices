from service_1.transactions import models
from service_1.transactions.settings import db_params

models.db.migrate(**db_params)
