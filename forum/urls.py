from django.urls import path
from forum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<int:id>/<str:slug>/', views.detail, name='detail'),
    path('create/', views.create_topic, name='create'),
    path('<int:topic_id>/comment/',views.post_comment, name='post_comment'),
]