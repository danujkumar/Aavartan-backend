"""backend URL Configuration

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
from django.urls import include, re_path
from server import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index),
    path('signup/<str:data>', v.signup),
    path('login/<str:data>', v.login),
    path('blindCode/<str:data>', v.blindCode),
    path('bow/<str:data>', v.bow),
    path('hydrolift/<str:data>', v.hydrolift),
    path('shipwreck/<str:data>', v.shipwreck),
    path('scavengerhunt/<str:data>', v.scavengerhunt),
    path('codetag/<str:data>', v.codetag),
    path('treasurehunt/<str:data>', v.treasurehunt),
    path('animatrix/<str:data>', v.animatrix),
    path('openmic/<str:data>', v.openmic)
]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
