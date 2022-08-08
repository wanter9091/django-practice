from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):#인자로 admin.StackedInline도 가능
    model= Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin):#이걸 해주면 내가 원하는 순서대로 정렬가능
    list_display=('question_text', 'pub_date', 'was_published_recently')#명시된 속성 출력(만약 잘못된 속성명 입력시 오류남)
    fieldsets=[#내부 데이터 출력
        (None,                  {'fields' : ['question_text']}),
        ('Date information',    {'fields' : ['pub_date']}),
    ]

    inlines=[ChoiceInline]#이 부분으로 Choice의 값도 변경 가능

    list_filter=['pub_date']#해당 속성에 대한 빠른 검색 선택지 추가
    search_fields=['question_text']#해당 속성에 대한 검색창 추가



admin.site.register(Question, QuestionAdmin)#이렇게 레지스터 함수를 사용해야 데이터를 어드민 페이지에서 데이터 수정 가능

# Register your models here.
