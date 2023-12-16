from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    return HttpResponse('hello world')

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'


