import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field='pub_date'#정렬 버튼을 눌렀을 때 정렬의 기준이 되는 속성 정하기
    was_published_recently.boolean=True#이 부분이 트루면 was_published_recently의 bool값이 true같은 문자형이 아닌 그림으로 표시됨
    was_published_recently.short_description='Published recently?'#출력되는 속성명을 변경

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text