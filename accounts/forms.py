from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    # Form to create new users, based on django model
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super(CreateUserForm, self).__init__(*args, **kwargs)
