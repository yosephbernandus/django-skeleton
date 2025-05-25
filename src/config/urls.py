from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    try:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass

    if settings.ENVIRONMENT == "local":
        from drf_spectacular.views import (
            SpectacularAPIView,
            SpectacularRedocView,
            SpectacularSwaggerView,
        )

        urlpatterns += [
            path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
            path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        ]
