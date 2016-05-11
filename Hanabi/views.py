import textwrap
import json

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from .game import Game


def index(request):
        hand = []
        players = ['mildlysauce', 'aaron', 'tyler', 'travis']
        game = Game(players)
        deckSize = game.deck.cardCount

        context = {
                'test': hand,
                'game': game,
                'deckSize': deckSize
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


def hello(request):
        if request.method == 'POST':
                game = request.POST['game']
        return HttpResponse(game.clues)
