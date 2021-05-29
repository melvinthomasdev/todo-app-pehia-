from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
# Create your views here.

# def homepageview(request):
#     return HttpResponse("""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Hello Django</title>
# </head>
# <body>
#     <h1> This is a Heading</h1>
#     <h2> This is another heading...</h2>
# </body>
# </html>""")


def homepageview(request):
    context = {}

    if request.POST:
        # print('The POST dictionary is: ', end=" ")
        # print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('desc')
        if (title and description):
            todo = Todo(title=title, description=description)
            todo.save()
    todos = Todo.objects.all()
    context['works'] = todos
    context['message'] = "Hello Sanjana, this is a message for you..."
    return render(request, 'index.html', context)


def TodoDetailView(request, tid):
    context = {}
    obj = Todo.objects.get(id=tid)
    context['todo'] = obj
    return render(request, 'detail.html', context)