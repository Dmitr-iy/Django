from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main page!!!',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 34,
            'hobby': 'serial'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
# Create your views here.

def blok(request):
    return render(request, 'main/blok.html')

def article(request):
    return render(request, 'main/article.html')