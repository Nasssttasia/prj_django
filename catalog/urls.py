from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, homepage, product
from django.conf import settings
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [
                  path('contacts/', contacts, name='contacts'),
                  path('', homepage, name='homepage'),
                  path('<int:pk>/product/', product, name='product'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # тоже что-то для картинок
