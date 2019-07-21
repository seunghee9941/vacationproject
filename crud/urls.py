from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name="home"),
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('comment/<int:pk>', views.comment, name="comment"),
    path('comment/<int:pk>/update/', views.comment_update, name="comment_update"),
    path('comment/<int:pk>/delete/', views.comment_delete, name="comment_delete"),
]
