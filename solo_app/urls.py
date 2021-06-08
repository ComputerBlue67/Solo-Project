from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('success',views.success),
    path('login',views.login),
    path('logout',views.logout),
    path('profile',views.profile),
    path('view-order',views.view_order),
    path('edit',views.edit),
]