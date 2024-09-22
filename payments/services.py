import stripe
from django.template.defaultfilters import title

from config.settings import STRIPE_APY_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_APY_KEY


# def convert_rub_to_dollars(payment_amount): ДАННАЯ БИБЛИОТЕКА так и не захотела работать
#     """Конвертирует рубли в доллары"""
#
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     return int(payment_amount * rate)

def create_stripe_product(course):
    """ Создает продукт в страйпе."""
    return stripe.Product.create(
    name=course.title,
    )


def create_stripe_price(product_id, payment_amount):
    """Создает цену в страйпе"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=payment_amount * 100,
        product=product_id,
    )


def create_stripe_session(price):
    """ Создает сессию на оплату в страйпе."""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
