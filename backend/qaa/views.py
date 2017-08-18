from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def questions(request):
  questions = Question.objects.all()
  output = ', '.join(p.__str__() for p in questions)
  return HttpResponse(output)
def question(request, question_id):
  id = int(question_id)
  question = Question.objects.get(id=id)
  return HttpResponse(question.__str__())