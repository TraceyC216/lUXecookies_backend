
from django.urls import path
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path('', views.cookies_list, name='index'),
    path('cookies/<int:id>/', views.category_detail, name='category_detail'),
    path('<str:category>/', views.category_list, name='category_index'),
    path('about/', views.about, name='about'),
    # re_path(r'^api/cookies/$', views.cookies_list),
    # re_path(r'^api/cookies/([0-9])$', views.cookies_detail),
    # path('traditional', views.traditional, name='traditional'),
    # path('allergy', views.allergy, name='allergy'),
    # path('decorated', views.decorated, name='decorated'),
    # 
    # path('create', views.create, name='create'),
 
]

