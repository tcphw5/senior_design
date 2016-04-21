import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render


def index(request):
        return render(request, 'index.html')


def statistics(request):
        return render(request, 'Statistics.html')


def rules(request):
        return render(request, 'Rules.html')


def landing(request):
        return render(request, 'Landing.html')


def joingame(request):
        return render(request, 'Join.html')
