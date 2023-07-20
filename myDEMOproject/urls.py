from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogapp.urls')),   # http://127.0.0.1:8000/tırnak içinde bir parametre belirtseydik onu buraya yazmamız gerekirdi/blog
    path('account/', include('account.urls'))

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
