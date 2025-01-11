from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='users/photo', verbose_name='Аватар', blank=True, null=True,
                               help_text='Загрузите свой аватар')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', blank=True,
                             null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=35, verbose_name='Страна', blank=True,
                               null=True, help_text='Введите страну')
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
