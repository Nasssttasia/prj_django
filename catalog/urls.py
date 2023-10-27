from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.conf import settings
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [
                  path('contacts/', contacts, name='contacts'),
                  path('', ProductListView.as_view(), name='homepage'),
                  path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
                  path('create/', ProductCreateView.as_view(), name='create'),
                  path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
                  path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # тоже что-то для картинок
