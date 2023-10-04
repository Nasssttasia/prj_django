from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import contacts, homepage

urlpatterns = [
                  path('contacts/', contacts),
                  path('', homepage),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # тоже что-то для картинок
