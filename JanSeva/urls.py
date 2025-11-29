from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- THIS LINE IS CRITICAL ---
    # It tells Django: "Send any link starting with 'api/home/' to the home app"
    path('api/home/', include('home.urls')),
    # -----------------------------
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)