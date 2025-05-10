from django.contrib import admin
from .models import Quiz, Question, Choice, QuizAttempt, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'quiz', 'order')
    list_filter = ('quiz',)
    search_fields = ('text',)


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True


class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'difficulty', 'question_count', 'created_at')
    list_filter = ('subject', 'difficulty')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]


class AnswerInline(admin.TabularInline):
    model = Answer
    readonly_fields = ('question', 'selected_choice', 'is_correct', 'ai_explanation')
    extra = 0
    can_delete = False


class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'started_at', 'completed_at', 'score')
    list_filter = ('quiz', 'user')
    readonly_fields = ('user', 'quiz', 'started_at', 'completed_at', 'score')
    inlines = [AnswerInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizAttempt, QuizAttemptAdmin)
