from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Company


# Create your views here.
class ListScheduleView(ListView):
    template_name = "schedule/schedule_list.html"
    model = Company
    
class DetailScheduleView(DetailView):
    template_name = "schedule/schedule_detail.html"
    model = Company
