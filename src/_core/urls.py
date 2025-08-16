"""
URL configuration for test_api project.

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Administration"

urlpatterns = [
    path("", include("django_prometheus.urls")),
    path("admin/", admin.site.urls, ),
    path("api/v1/products/", include("products.api.v1.urls", namespace="products")),
]

if settings.DEBUG:

    urlpatterns += [
        path("api/__debug__/", include("debug_toolbar.urls")),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
