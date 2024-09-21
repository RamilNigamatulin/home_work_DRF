import stripe
from config.settings import STRIPE_APY_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_APY_KEY


# def convert_rub_to_dollars(payment_amount): ДАННАЯ БИБЛИОТЕКА так и не захотела работать
#     """Конвертирует рубли в доллары"""
#
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     return int(payment_amount * rate)


def create_stripe_price(payment_amount):
    """Создает цену в страйпе"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=payment_amount * 100,
        product_data={"name": "Gold Plan"},
    )


def create_stripe_session(price):
    """ Создает сессию на оплату в страйпе."""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')