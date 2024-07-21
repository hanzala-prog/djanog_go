"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as accounts_views
from articles import views as articles_views

from .views import home_view

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', home_view),
    path('articles/', articles_views.article_search_view),
    path('articles/create/', articles_views.article_create_view, name='article_create'),
    path('articles/<int:id>/', articles_views.article_detail_view, name='article_detail'),
    path('theboss/', admin.site.urls), # admin
    path('register/', accounts_views.register_view),
    path('login/', accounts_views.login_view),
    path('logout/', accounts_views.logout_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

