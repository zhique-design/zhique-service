"""ZhiQue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

from ZhiQue import permissions
from ZhiQue.admin_site import admin_site
from oauth.views import LoginView, AuthorizeView, LogoutView

schema_view = get_schema_view(
    openapi.Info(
        title='知雀',
        default_version='v1',
        description='知雀接口文档',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
                  path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('admin/', admin_site.urls),
                  re_path(r'^(?P<version>(v1|v2))/account/', include('account.urls', namespace='account')),
                  re_path(r'^(?P<version>(v1|v2))/blog/', include('blog.urls', namespace='blog')),
                  re_path(r'^oauth/login$', LoginView.as_view(), name='login'),
                  re_path(r'^oauth/logout$', LogoutView.as_view(), name='logout'),
                  re_path(r'^oauth/(?P<authorize_type>[a-z]+)/authorize/$', AuthorizeView.as_view(), name='authorize'),
                  re_path(r'^(?P<version>(v1|v2))/attachment/', include('attachment.urls', namespace='attachment')),
                  re_path(r'^(?P<version>(v1|v2))/console/', include('console.urls', namespace='console')),
                  re_path(r'^(?P<version>(v1|v2))/common/', include('common.urls', namespace='common')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
