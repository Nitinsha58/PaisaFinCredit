from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.views import index

urlpatterns = (
    [
        path("", index, name="home"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns.extend(
        (
            path("admin/", admin.site.urls),
            path("__debug__/", include(debug_toolbar.urls)),
        )
    )
