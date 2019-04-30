from .views import home_page, transactions, create_transaction_view


def setup_routes(app):
    """
    :param app:
    :return:
    """
    app.router.add_get('/', home_page, name='home_page')
    app.router.add_post('/create-transaction/', create_transaction_view, name='create_transaction')
    app.router.add_get('/transactions/', transactions, name='transactions')
