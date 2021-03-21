from django.shortcuts import render, redirect
from appregionalidade.forms import ContatoForm
from appregionalidade.models import Contatos
# Create your views here.

def home(request):
    data = {}
    data['db'] = Contatos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ContatoForm()
    return render(request, 'form.html', data)

def create(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Contatos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Contatos.objects.get(pk=pk)
    data['form'] = ContatoForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data= {}
    data['db'] = Contatos.objects.get(pk=pk)
    form= ContatoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Contatos.objects.get(pk=pk)
    db.delete()
    return redirect('home')