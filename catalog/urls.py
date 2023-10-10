from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, homepage, product

app_name = CatalogConfig.name

urlpatterns = [
                  path('contacts/', contacts, name='contacts'),
                  path('', homepage, name='homepage'),
                  path('<int:pk>/product/', product, name='product'),

              ]
