from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создание обычного пользователя
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields) # Создает экземлпяр класса 
        user.set_password(password) # Хеширует пароль
        user.save(using=self._db) # Сохроняет в БД
        return user # Возвращает экземпляр 

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создание супер пользователя
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
    def create(self, **kwargs):
        return self.create_user(**kwargs)

class CustomUser(AbstractUser):
    """
    Модель CustomUser, которая расширяет модель AbstractUser.

    Атрибуты:
        username (CharField): Имя пользователя, должно быть уникальным и иметь максимальную длину 150 символов.
        email (EmailField): Адрес электронной почты пользователя, должен быть уникальным.
        phone_number (CharField): Номер телефона пользователя, может быть пустым или нулевым, с максимальной длиной 20 символов.
        is_active (BooleanField): Указывает, активен ли пользователь, по умолчанию False.
        auth_code (CharField): 6-символьный код аутентификации, может быть пустым или нулевым.

    Meta:
        USERNAME_FIELD (str): Указывает поле, которое будет использоваться в качестве уникального идентификатора, установлено на 'email'.
        REQUIRED_FIELDS (list): Указывает поля, необходимые для создания пользователя, установлено на ['username'].

    Методы:
        __str__(): Возвращает адрес электронной почты пользователя в качестве строкового представления.
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    auth_code = models.CharField(max_length=6, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
