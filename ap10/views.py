from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('home.html')
    context = {
      'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))

def second(request):
    template = loader.get_template('second.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))
