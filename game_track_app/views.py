from django.shortcuts import render
from django.template import loader
from django.db.models.functions import Lower
from django.http import HttpResponse

import django.db.models as models

from .models import Game, User, GameStat


def index(request):
    game_list = Game.objects.order_by(Lower('name'))
    owned_list = Game.objects.filter(gamestat__user=User.objects.get(name="John Bucknam"))

    # test_list = Game.objects.filter(gamestat__isnull=True).values_list('name', flat=True)
    # print(test_list)

    test_list = Game.objects.annotate(
        owned=models.Case(
            models.When(gamestat__game_id=None, then=models.Value(False)),
            default=models.Value(True)
        ),
    ).values_list('name', 'owned').values('name', 'owned').order_by(Lower('name'))

    template = loader.get_template("game_track_app/index.html")
    context = {'game_list': test_list}
    return HttpResponse(template.render(context, request))
