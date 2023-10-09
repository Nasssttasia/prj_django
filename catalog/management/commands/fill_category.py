from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'title': 'еда', 'description': 'вкусная еда'},
            {'title': 'одежда', 'description': 'красивая одежда'},
            {'title': 'книги', 'description': 'интересные книги'},
            {'title': 'косметика', 'description': 'дорогая косметика'}
        ]

        category_to_create = []
        for category_items in category_list:
            category_to_create.append(
                Category(**category_items)
            )

        Category.objects.bulk_create(category_to_create)
