from django.shortcuts import render

def index(request):
    context = {}
    context['hello'] = 'Hello world' #这个hello的key对应着之前在templates/index.html中写入的元素hello
    return render(request, 'index.html', context)
