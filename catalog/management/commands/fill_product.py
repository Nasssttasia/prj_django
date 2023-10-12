from django.core.management import BaseCommand
from datetime import datetime
from catalog.models import Product, Category


class Command(BaseCommand):


    def handle(self, *args, **options):

        products = [
            {'title': 'хлеб', 'description': 'свежий хлеб', 'category': 'еда', 'price': '60', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'майка', 'description': 'красивая майка', 'category': 'одежда', 'price': '1000', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'маленький принц', 'description': 'интересная книга', 'category': 'книги', 'price': '600', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'тушь', 'description': 'черная тушь', 'category': 'косметика', 'price': '1000', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
        ]

        product_to_create = []

        # Перебираем продукты для изменения
        for product in products:
            # Получаем категорию
            category_title = product.get('category')
            category = Category.objects.get(title=category_title)

            # Изменяем категорию продукта на значение из базы данных
            product = product['category'] = category

            # Приводим дату к виду YYYY-MM-DD
            product['date_of_change'] = datetime.strptime(product['date_of_change'], '%d.%m.%Y').strftime('%Y-%m-%d')
            product['date_of_creation'] = datetime.strptime(product['date_of_creation'], '%d.%m.%Y').strftime('%Y-%m-%d')

            # Добавляем продукты в новый список
            product_to_create.append(
                Product(**product)
            )



        Product.objects.bulk_create(product_to_create)
