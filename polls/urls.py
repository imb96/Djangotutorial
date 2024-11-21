# Django의 URL 패턴을 정의하는 기능
from django.urls import path

# 같은 디렉토리에 있는 views.py 불러오기
from . import views

# URL 패턴 정의하는 목록
urlpatterns = [
    # path(URL 경로, 뷰 함수, URL이름)
    path("", views.index, name="index"),
]
