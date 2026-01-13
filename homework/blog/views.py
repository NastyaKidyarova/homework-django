from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
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


def feedback_list(request):
    feedbacks = Feedback.objects.filter(checked=True)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()

    return render(request, 'blog/feedback_list.html', {'feedbacks': feedbacks, 'form': form})
