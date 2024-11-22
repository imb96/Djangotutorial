from django.shortcuts import render # HTML 템플릿을 보여주는 기능
from django.http import HttpResponse # HTTP 응답을 보내는 기능
from .models import Question
# Create your views here.

# index라는 view 함수 생성. 웹 요청이 들어왔을 때 실행되는 함수.
def index(request): # request는 사용자의 요청을 담고있는 객체
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  output = ", ".join([q.question_text for q in latest_question_list])
  return HttpResponse(output)

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)