from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('travello.urls')),  # Assuming travello is another app
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # This correctly includes accounts/urls.py
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
