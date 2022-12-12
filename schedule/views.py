from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Company


# Create your views here.
class ListScheduleView(ListView):
    template_name = "schedule/schedule_list.html"
    model = Company
    
class DetailScheduleView(DetailView):
    template_name = "schedule/schedule_detail.html"
    model = Company
    
class CreateScheduleView(CreateView):
    template_name = "schedule/schedule_create.html"
    model = Company
    fields = ("company_name", "business", "memo", "hp_url", "rikunabi_url", "mainabi_url")
    success_url = reverse_lazy("list-schedule")
    
class DeleteScheduleView(DeleteView):
    template_name = "schedule/schedule_delete.html"
    model = Company
    success_url = reverse_lazy("list-schedule")
