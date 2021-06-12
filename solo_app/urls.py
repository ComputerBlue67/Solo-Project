from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('success',views.success),
    path('login',views.login),
    path('logout',views.logout),
    path('view-profile',views.view_profile),
    path('edit-profile',views.edit_profile),
    path('delete-profile',views.delete_profile),
    path('view-menu',views.view_menu),
    path('share',views.share),
    path('add-image',views.add_image),
    # path('delete-image',views.delete_image),
]