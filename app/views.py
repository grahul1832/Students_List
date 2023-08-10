from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy


class SchoolList(ListView):
    model=School
    context_object_name='ALLSO'
      

class SchoolDetail(DetailView):
    model=School
    context_object_name='aabb'
    template_name='app\school_details.html'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'
    

class Update(UpdateView):
    model=School
    fields='__all__'



class SchoolDelete(DeleteView):
    model=School
    context_object_name='dso'
    success_url=reverse_lazy('SchoolList')
