from django.http import HttpResponse
from django.template import loader

def home(request):
    template=loader.get_template('my_home.html')
    return HttpResponse(template.render())

