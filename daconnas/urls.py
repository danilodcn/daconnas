
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from web.views import home_web


urlpatterns = [
    path("index", home_web, name="home_url"),
    path('admin/', admin.site.urls),
    # path("web/", include("web.urls")),
    path("api/", include("api.urls")),
    path("web/", include("core.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
