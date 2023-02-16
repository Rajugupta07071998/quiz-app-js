from django.contrib import admin

# Register your models here.

from .models import *

class QuizAdmin(admin.ModelAdmin):
    list_display=['id','question','option1','option2','option3','option4','answer']


class QuizQuestionsAdmin(admin.ModelAdmin):
    list_display=['id','question_text']

class QuizAnswersAdmin(admin.ModelAdmin):
    list_display=['answer_text', 'is_correct','question']

class QuizCorrectAnswersAdmin(admin.ModelAdmin):
    list_display=['id','answer']




admin.site.register(Quiz_Table, QuizAdmin)
admin.site.register(QuizQuestions, QuizQuestionsAdmin)
admin.site.register(QuizAnswers, QuizAnswersAdmin)
admin.site.register(QuizCorrectAnswers, QuizCorrectAnswersAdmin)
admin.site.register(State)
admin.site.register(City)



