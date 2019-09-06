from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from adoptions import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail'),
]

