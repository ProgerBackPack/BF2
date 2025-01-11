from django.db import models

from doctors.models import Doctor
from users.models import User


class Service(models.Model):
    name = models.CharField(max_length=250, verbose_name='Услуга')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    picture = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="Услуги")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="Доктор")
    created_at = models.DateTimeField(auto_now_add=True)
    record_time = models.DateField(verbose_name='Дата записи')
    is_active = models.BooleanField(default=True, verbose_name='Отмена записи')

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} записан на {self.service.name} к {self.doctor}."

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        permissions = [
            ('can_add_record', 'Может добавлять запись'),
            ('can_change_record', 'Может изменять запись'),
            ('can_view_record', 'Может просматривать запись'),
            ('can_delete_record', 'Может удалять запись'),
        ]


class Diagnostic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    record = models.ForeignKey(Record, on_delete=models.CASCADE, verbose_name="Запись")
    result = models.TextField(verbose_name='Результат')
    diagnose = models.CharField(max_length=250, verbose_name='Диагноз')

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} результат {self.record.service}."

    class Meta:
        verbose_name = 'Диагностика'
        verbose_name_plural = 'Диагностики'
        permissions = [
            ('can_view_diagnostics', 'Может просматривать диагностики'),
        ]
