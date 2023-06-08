from django.contrib.auth import authenticate, login, update_session_auth_hash,logout
from django.contrib.auth.views import PasswordChangeView
from django.views import View
from home.views import HomeView
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, UserProfileForm, ChangePasswordForm
from .models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404



class RegisterView(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'register.html', {'form': form})

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
# 用户注销
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')  # 你需要把 'home' 替换成你的首页视图的名称

class UserProfileView(View):
    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'profile.html', {'form': form})

    def get(self, request):
        form = UserProfileForm(instance=request.user.userprofile)
        return render(request, 'profile.html', {'form': form})


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = '/profile'
    template_name = 'change_password.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.request.user)
        return response


# 用户控制面板
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # 你可能需要从数据库中获取一些数据，比如用户的帖子，商品，收藏等，然后传递给模板
        return render(request, 'dashboard.html')


# # 用户通知和消息。这只是一个基本的实现，你可能需要根据你的业务逻辑进行修改
# class UserNotificationsView(LoginRequiredMixin, View):
#     def get(self, request):
#         # 你需要自己实现获取用户通知的逻辑
#         return render(request, 'notifications.html')

#     def post(self, request):
#         # 你需要自己实现发送用户通知的逻辑
#         pass


# 用户统计和报告。你可能需要根据你的业务逻辑修改这个视图
class UserAnalyticsView(LoginRequiredMixin, View):
    def get(self, request):
        user_count = UserProfile.objects.count()
        return render(request, 'analytics.html', {'user_count': user_count})