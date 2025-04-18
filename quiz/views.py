from django.shortcuts import render
from .models import Question, Level, Answer

# Create your views here.


def start_game(request):
    questions = Question.objects.all()

    return render(request, "start_game.html", {"questions": questions})
