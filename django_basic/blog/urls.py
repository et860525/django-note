from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail'),
]
