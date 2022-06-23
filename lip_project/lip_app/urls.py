from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('success',views.success),
    path('login',views.login),
    path('logout',views.logout),
    path('addbook',views.addbook),
    path('books/<int:id>',views.show_book),
    path('update_book/<int:id>',views.update_book),
    path('delete_book/<int:id>',views.delete_book),
    path('likebook/<int:id>',views.like_book),
    path('unlikebook/<int:id>',views.unlike_book),

    
]