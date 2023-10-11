from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    category = Category.objects.all()

    def handle(self, *args, **options):
        product_list = [
            {'title': 'хлеб', 'description': 'свежий хлеб', 'category': 'еда', 'price': '60', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'майка', 'description': 'красивая майка', 'category': 'одежда', 'price': '1000', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'маленький принц', 'description': 'интересная книга', 'category': 'книги', 'price': '600', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
            {'title': 'тушь', 'description': 'черная тушь', 'category': 'косметика', 'price': '1000', 'date_of_creation': '09.10.2023', 'date_of_change': '09.10.2023'},
        ]

        product_to_create = []
        for product_items in product_list:
            product_to_create.append(
                Product(**product_items)
            )

        Product.objects.bulk_create(product_to_create)
