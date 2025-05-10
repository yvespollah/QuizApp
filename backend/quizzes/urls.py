from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuizAttemptViewSet, UserQuizHistoryView

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'attempts', QuizAttemptViewSet, basename='attempt')

urlpatterns = [
    path('', include(router.urls)),
    path('history/', UserQuizHistoryView.as_view(), name='quiz-history'),
]
