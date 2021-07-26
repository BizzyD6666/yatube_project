from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Посты')


def group_post_detail(request, slug):
    return HttpResponse(f'Пост  {slug}')
