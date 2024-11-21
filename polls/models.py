import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Question 모델 (설문조사 질문)
class Question(models.Model):
  question_text = models.CharField(max_length=200) # 문자열을 저장하는 필드(최대 200자까지 저장 가능)
  pub_date = models.DateTimeField('date published') # 날짜와 시간을 저장하는 필드(관리자 페이지에서 보여질 이름)
  def __str__(self):
    return self.question_text
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice 모델 (설문조사 선택지)
class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키 관계 설정. Question 모델과 연결. 삭제되면 CASCADE 옵션에 따라 관련된 Choice 객체도 삭제
  choice_text = models.CharField(max_length=200) # 문자열을 저장하는 필드(최대 200자까지 저장 가능)
  votes = models.IntegerField(default=0) # 정수를 저장하는 필드(기본값은 0)
  def __str__(self):
    return self.choice_text