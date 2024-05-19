import pika
import json
from threading import Thread
from domain.model.product_domain import Product_domain
from infraestructure.repository.product_repository_impl import Product_repository_imp
from application.service.product_service import Product_service
from infraestructure.configuration.rabbit import Rabbit

repository = Product_repository_imp()
service = Product_service(repository)


def callback(ch, method, properties, body):
    data = json.loads(body)
    products_data = data.get('products', [])
    products = [Product_domain(**product) for product in products_data]
    service.update_product(products)


def start_listening():
    rabbit = Rabbit()
    rabbit.channel.basic_consume(
        queue='order_updates',
        on_message_callback=callback,
        auto_ack=True
    )
    thread = Thread(target=rabbit.channel.start_consuming)
    thread.start()
