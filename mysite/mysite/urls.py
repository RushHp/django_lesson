
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # namespace="myapp" - имя приложения используемое в шаблонах, что бы не было конфликта имен.
    path('myapp/', include('myapp.urls', namespace="myapp"))
]
 