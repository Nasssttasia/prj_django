from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):


    def handle(self, *args, **options):

        product = [
            {'title': 'хлеб', 'description': 'свежий хлеб', 'category': 'еда', 'price': '60', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'майка', 'description': 'красивая майка', 'category': 'одежда', 'price': '1000', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'маленький принц', 'description': 'интересная книга', 'category': 'книги', 'price': '600', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'тушь', 'description': 'черная тушь', 'category': 'косметика', 'price': '1000', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
        ]

        category_title = product.get('category')
        category = Category.objects.get(title=category_title)
        product = product['category'] = category

        product_to_create = []
        for product_items in product:
            product_to_create.append(
                Product(**product_items)
            )

        Product.objects.bulk_create(product_to_create)
