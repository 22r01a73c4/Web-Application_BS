# main/views.py
from django.shortcuts import render
from .models import IPO

def upcoming_ipos(request):
    ipos = IPO.objects.all()
    return render(request, 'upcoming_ipos.html', {'ipos': ipos})
