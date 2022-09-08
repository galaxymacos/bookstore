from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create two forms for custom user model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()    # Get the custom user model because settings.py has AUTH_USER_MODEL = "accounts.CustomUser"
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
