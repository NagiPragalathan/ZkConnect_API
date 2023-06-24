"""ZkConnect URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from backend.Routes import views, tools
from ZkConnect import settings

urlpatterns = []

common = [
    path('home', views.home),
    path('', views.welcome_home),
    path('admin/', admin.site.urls),
]

tools_fn = [
    path('get_user_data', tools.get_user_data),
]

login_fn = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_fn, name='login'),
]

urlpatterns = urlpatterns + common + login_fn
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
