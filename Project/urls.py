from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('user/<int:user_id>/', views.details, name='details'),
    path('user/<int:user_id>/delete/', views.delete, name='delete_user'),
    path('add/', views.add_customer , name='add_customer'),
    path('user/<int:user_id>/update/', views.update_customer, name='update_user'),
]
