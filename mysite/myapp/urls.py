from django.urls import path
from myapp.views import index, index_item

# Имя приложения используемое в шаблонах, что бы не было конфликта имен.
app_name = "myapp"

urlpatterns = [
    path('', index),
    # Динамический путь.
    path('<int:id>/', index_item, name="detail"),
]
