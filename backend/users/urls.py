from django.urls import path
from .views import RegisterView, UserDetailView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
