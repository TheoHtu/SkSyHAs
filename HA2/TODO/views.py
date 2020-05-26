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
        return TODO.objects.order_by('deadline')

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
    print("added " + request.POST['name'])
    if fortschritt == '':
        fortschritt = 0
    td = TODO(name=name, deadline=deadline, fortschritt=fortschritt)
    td.save()
    return redirect('main')

def edit(request):
    #context_object_name = 'TODO_list'

    print("editing "+ request.POST['id'])
    return render(request,'TODO/main.html',{'TODO_list':TODO.objects.order_by('deadline'),'editid':int(request.POST['id'])})

def save(request):
    id = request.POST['id']
    try:
        td = TODO.objects.get(id=id)
    except:
        return redirect('main')
    else:
        td.name = request.POST['name']
        td.deadline = request.POST['deadline']
        td.fortschritt = request.POST['fortschritt']
        td.save()
        return redirect('main')

def delete(request):
    id = request.POST['id']
    try:
        td = TODO.objects.get(id=id)
    except:
        return redirect('main')
    else:
        print("deleted "+id)
        td.delete()
        return redirect('main')
    