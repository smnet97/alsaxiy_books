from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Alsaxiy Books API",
        default_version='1.0.0',
        description="Alsaxiy books oline shop app",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',
         include([
             path('', include('users.urls')),
             path('', include('books.urls')),
             path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
         ])
         ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
