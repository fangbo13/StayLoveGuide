from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser, UserProfile

# 用户注册
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

# 用户登录
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]

# 用户个人资料
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar", "bio", "location"]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
        }

# 密码管理
class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password1", "new_password2"]
    