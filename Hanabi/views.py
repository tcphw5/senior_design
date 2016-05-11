import textwrap
import json

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import render
from django.shortcuts import redirect
from .game import Game


def index(request, playernames):
        players = playernames.split('/')
        hand = []
        game = Game(players)
        deckSize = game.deck.cardCount
        remdeck = game.deck

        context = {
                'test': hand,
                'game': game,
                'deckSize': deckSize,
                'remdeck': remdeck

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
        player1 = request.POST['player1']
        player2 = request.POST['player2']
        player3 = request.POST['player3']
        player4 = request.POST['player4']
        playernames = (player1+"/"+player2+"/"+player3+"/"+player4)

        return HttpResponseRedirect(reverse('Hanabi:index', args=(playernames, )))
