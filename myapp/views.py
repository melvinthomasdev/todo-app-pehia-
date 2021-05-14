from django.shortcuts import render
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
    todos = Todo.objects.all()
    context['works'] = todos
    context['message'] = "Hello Sanjana, this is a message for you..."
    return render(request, 'index.html', context)
