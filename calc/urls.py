from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('detail', views.detail, name='detail'),
    path('chennai_past', views.chennai_past, name='chennai_past'),
    path('solapur_past', views.solapur_past, name='solapur_past'),
    path('register', views.register, name='register'),
]

