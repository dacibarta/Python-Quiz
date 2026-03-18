from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from quiz.models import Question, Answer
import os


def index(request):
    return HttpResponse(loader.get_template("index.html").render({}, request))


def add_question(request):
    return HttpResponse(loader.get_template("question.html").render({}, request))


def add_question_record(request):
    new_question = Question(text=request.POST.get("question"))
    new_question.save()

    Answer(
        question=new_question, text=request.POST.get("correct"), is_correct=True
    ).save()
    Answer(question=new_question, text=request.POST.get("wrong1")).save()
    Answer(question=new_question, text=request.POST.get("wrong2")).save()
    Answer(question=new_question, text=request.POST.get("wrong3")).save()

    messages.success(request, "A kérdés sikeresen elmentve!")
    return HttpResponseRedirect(reverse("index"))
