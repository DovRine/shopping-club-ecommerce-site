from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('public.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
