Authentication:
1] User Model: 
Django provides a built-in User model for authentication purposes. 
It includes fields for username, password, email, first name, and last name.

    from django.contrib.auth.models import User

2] Authentication Views: 
Django includes views for login, logout, and password management:

LoginView for logging users in
LogoutView for logging users out
PasswordChangeView and PasswordResetView for changing and resetting passwords

    from django.contrib.auth.views import LoginView, LogoutView

3] Forms: 
Django also provides forms for user authentication, such as AuthenticationForm for logging in and UserCreationForm for creating new users.

    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

4] Authentication Middleware: 
The AuthenticationMiddleware is responsible for associating users with requests.

    MIDDLEWARE = [
    ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
]

======================================================================================

Authorization:
1] Permissions: 
Django’s User model has a built-in permissions framework that allows you to assign permissions to users and groups. You can define custom permissions in your models.

    class MyModel(models.Model):
    ...
    class Meta:
        permissions = [
            ("can_edit_mymodel", "Can edit my model"),
        ]
2] Groups: 
You can group users and assign permissions to these groups. This way, you can manage permissions more easily for multiple users.

    from django.contrib.auth.models import Group

3] Decorators: 
Django provides decorators like login_required, permission_required, and user_passes_test to restrict access to views based on authentication status or permissions.

    from django.contrib.auth.decorators import login_required, permission_required

4] Mixins: 
For class-based views, Django provides mixins like LoginRequiredMixin and PermissionRequiredMixin to enforce access control.

    from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

    Ex:..
    class MyView(LoginRequiredMixin, View):
    ...

5] Permissions System: 
Django also provides a flexible permissions system where you can check for specific permissions within your views or templates.

    if request.user.has_perm('myapp.can_edit_mymodel'):
        ...
