from django.shortcuts import render
from django.views.generic import ListView
from .models import Company


# Create your views here.
class ScheduleBoardView(ListView):
    template_name = "schedule/scheduleboard.html"
    model = Company
