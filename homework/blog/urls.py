from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # О блоге
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Страница поста
    path('feedback/', views.feedback_list, name='feedback_list'), # Страница с отзывами
]
