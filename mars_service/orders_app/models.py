from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from datetime import datetime 
# Create your models here.

class Device(models.Model):
    """ Обладнання """

    class Meta:
        db_table = 'devices'
        verbose_name = 'Доступне обладнання '
        verbose_name_plural = 'Доступне обладнання'

    manufacturer = models.TextField(verbose_name='Виробник')
    model = models.TextField(verbose_name='Модель')

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
 
 
class Customer(models.Model):
    """Кінцеві користувачі обладнання""" 

    class Meta:
        db_table = 'customers'
        verbose_name = 'Опис контрагента'
        verbose_name_plural = 'Опис контрагентів'

    customer_name = models.TextField(verbose_name='Назва організації')
    customer_address = models.TextField(verbose_name='Адреса')
    customer_city = models.TextField(verbose_name='Місто')

    def __str__(self):
        return f"{self.customer_name} по адресі {self.customer_address}"


class DeviceInField(models.Model):
    """Обладнання в полях"""
    class Meta:
        db_table = 'devices_in_fields'
        verbose_name = 'Обладнання в полях'
        verbose_name_plural = 'Обладнання в полях'

    serial_number = models.TextField(verbose_name='Серійний номер')
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Ідентифікатор користувача')
    analyzer = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name='Ідентифікатор обладнання ')
    owner_status = models.TextField(verbose_name='Статус власності ')

    def __str__(self):
        return f"{self.analyzer} с/н  {self.serial_number} в {self.customer}"





class Order(models.Model):
    """Опис заявки"""
    class Meta:
        db_table = 'orders'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


    statuses = (
        ("open", "відкрита"),
        ("closed", "закрита"),
        ("in progress", "в роботі"),
        ("need info", "потрібна інформація")
    )
    device = models.ForeignKey(DeviceInField, verbose_name='Обладнання', on_delete=models.RESTRICT)
    order_description = models.TextField(verbose_name='Опис')
    created_dt = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
    last_updated_dt=models.DateTimeField(verbose_name='Остання зміна', blank=True, null=True)
    order_status = models.TextField(verbose_name='Статус заявки', choices=statuses)
    
    def __str__(self):
        return f"Заявка № {self.id} для {self.device}"

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)

















