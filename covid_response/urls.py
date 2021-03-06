"""covid_response URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from user import views
from user.views import FakeNewsChatBotAPI, CovidUpdatesAPI, RegistrationAPI, LoginAPI, SlotCheckAPI, ShopListAPI, shop_list, SlotConfirmAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatBot/', FakeNewsChatBotAPI.as_view()),
    path('update/', CovidUpdatesAPI.as_view()),
    path('register/', RegistrationAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('slotCheck/',SlotCheckAPI.as_view()),
    path('shopList/',ShopListAPI.as_view()),
    path('confirmSlot/',SlotConfirmAPI.as_view())
]
