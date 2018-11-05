"""
webvirtcloud URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title='WebVirtCloud API')

    urlpatterns += [
        path('swagger/', schema_view, name='api_docs'),
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# SPA
urlpatterns += [
    # path('.*$', never_cache(IndexView.as_view()), name='index'),
]
