"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from web.routers import router as router_web
from web.views import PingView
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('ping/', PingView.as_view(), name="ping"),
    path('api-auth/', include('rest_framework.urls')),
    path('web/', include(router_web.urls)),
    path('openapi', get_schema_view(
        title="Cibertec",
        description="API for students",
        version="0.0.1"
    ), name='openapi-schema'),
    path("__debug__/", include("debug_toolbar.urls")),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
]
