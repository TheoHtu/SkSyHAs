# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.http import HttpResponseRedirect

from .models import TODO
from .forms import CreateForm


class Main(generic.ListView):
    template_name = 'TODO/main.html'
    context_object_name = 'TODO_list'
    def get_queryset(self):
        return TODO.objects.all()

class Add(generic.CreateView):
    model = TODO
    fields = ['name','deadline','fortschritt']
    template_name = 'TODO/add.html'

class Impressum(generic.TemplateView):
    template_name = 'TODO/impressum.html'

def new_todo(request):
    name = request.POST['name']
    deadline = request.POST['deadline']
    fortschritt = request.POST['fortschritt']
    print(request.POST)
    if fortschritt == '':
        fortschritt = 0
    td = TODO(name=name, deadline=deadline, fortschritt=fortschritt)
    td.save()
    return redirect('main')

def edit(request):
    for i in request.POST:
        print(i)
    return redirect('main')

def delete(request):
    id = request.POST['id']
    try:
        td = TODO.objects.get(id=id)
    except:
        return redirect('main')
    else:
        td.delete()
        return redirect('main')
    