from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogapp.urls')),   # http://127.0.0.1:8000/tırnak içinde bir parametre belirtseydik onu buraya yazmamız gerekirdi /blog

]
