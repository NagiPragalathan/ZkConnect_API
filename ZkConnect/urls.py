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
from backend.Routes import views, tools, bot, profile, storage, cam
from ZkConnect import settings

urlpatterns = []

common = [
    path('home', views.home),
    path('', views.welcome_home),
    path('admin/', admin.site.urls),
]

tools_fn = [
    path('get_profile_data', tools.get_profile_data),
]

login_fn = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_fn, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
]
company = [
    path('store_company_details', profile.Store_Company_Details, name='store_company_details'),
]
bot_res = [
    path('chatbot_res/', bot.chatbot_res, name='chatbot_res'),
]

profile_fn = [
    path('profile/', profile.profile_data, name='profile'),
    path('Rec_Profile_data/', profile.Rec_Profile_data, name='Rec_Profile_data'),
    path('clim_data/', profile.clim_data, name='clim_data'),
]

DB3 = [
    path('upload_img_file/', storage.upload_file, name='upload_img_file'),
    path('store_pdf/', storage.store_pdf, name='store_pdf'),
    path('retrieve_pdf/', storage.retrieve_pdf, name='retrieve_pdf'),
    
    # path('head_pose_estimation/', cam.head_pose_estimation, name='head_pose_estimation'),
]


urlpatterns = urlpatterns + common + login_fn + tools_fn + bot_res + profile_fn + DB3 +company
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
