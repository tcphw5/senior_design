import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from .game import Game


def index(request):
        hand = []
        players = ['mildlysauce', 'aaron', 'tyler', 'travis']
        hand.append('y1')
        hand.append('y1')
        hand.append('y1')
        hand.append('y1')
        hand.append('y1')
        game = Game(players)

        context = {
                'test': hand,
                'game': game
        }

        return render(request, 'index.html', context)


def statistics(request):
        return render(request, 'Statistics.html')


def rules(request):
        return render(request, 'Rules.html')


def landing(request):
        return render(request, 'Landing.html')


def joingame(request):
        return render(request, 'Join.html')
