from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('comment/<int:id>/delete/', views.delete_comment, name='delete_comment'),

]
