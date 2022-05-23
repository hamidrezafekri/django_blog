from django.http import HttpResponse

def hello_world_view(request):
    return HttpResponse('hello world')
    