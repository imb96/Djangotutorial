from django.shortcuts import render # HTML 템플릿을 보여주는 기능
from django.http import HttpResponse # HTTP 응답을 보내는 기능
# Create your views here.

# index라는 view 함수 생성. 웹 요청이 들어왔을 때 실행되는 함수.
def index(request): # request는 사용자의 요청을 담고있는 객체
  return HttpResponse("Hello, world. PY~") # 사용자에게 응답