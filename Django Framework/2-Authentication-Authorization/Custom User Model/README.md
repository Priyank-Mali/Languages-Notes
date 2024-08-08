1] Custom User Models: 
If the default User model doesn’t meet your needs, you can create a custom user model by extending AbstractUser or AbstractBaseUser.

    from django.contrib.auth.models import AbstractUser

    class MyUser(AbstractUser):
        ...
