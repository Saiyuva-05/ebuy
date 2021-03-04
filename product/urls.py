from django.urls import path
from . import views
app_name = 'single'
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cloath/', views.cloath, name='cloath'),
    #path('cloath/<int:t_id>/tracking/', views.tracking, name='tracking'),
    #path('electronic/<int:t_id>/tracking/', views.tracking, name='tracking'),
    #path('tracking/', views.tracking, name='tracking'),
    path('electronic/', views.electronic, name='electronic'),
    path('cloath/<int:p_id>/', views.detail, name='detail'),
    path('electronic/<int:e_id>/', views.elect_detail, name='elect_detail'),
]
