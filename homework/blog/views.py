from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def home(request):
    return render(request, 'blog/home.html')

# Страница "О блоге"
def about(request):
    return render(request, 'blog/about.html')

# Страница поста
def post_detail(request, post_id):
    # Здесь можно сделать запрос в базу данных для получения поста по ID
    # Для простоты создадим статические данные:
    post = {
        'id': post_id,
        'title': f'Пост {post_id}',
        'content': 'Контент поста будет здесь.'
    }
    return render(request, 'blog/post_detail.html', {'post': post})
