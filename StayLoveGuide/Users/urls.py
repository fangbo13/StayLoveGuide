from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, ChangePasswordView, LogoutView, DashboardView, UserAnalyticsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('analytics/', UserAnalyticsView.as_view(), name='analytics'),
    # 在这里添加你的其他 URL
]
