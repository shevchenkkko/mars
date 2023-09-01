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
        return self.customer_name


class DeviceInField(models.Model):
    """Обладнання в полях"""
    class Meta:
        db_table = 'devices_in_fields'
        verbose_name = 'Обладнання в полях'
        verbose_name_plural = 'Обладнання в полях'

    serial_number = models.TextField(verbose_name='Серійний номер')
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Ідентифікатор користувача')
    analyzer_id = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name='Ідентифікатор обладнання ')
    owner_status = models.TextField(verbose_name='Статус власності ')

    def __str__(self):
        return f"{self.serial_number} {self.analyzer_id}"



def status_validator(order_status):
    if order_status not in ['open', 'closed', 'in progress', 'need info']:
        raise ValidationError(
            gettext_lazy('%(order_status)s is wrong order status'),
            params={'order_status':order_status},
        )


class Order(models.Model):
    """Опис заявки"""
    class Meta:
        db_table = 'orders'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    device = models.ForeignKey(DeviceInField, verbose_name='Обладнання', on_delete=models.RESTRICT)
    customer= models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Кінцевий користувач')
    order_description = models.TextField(verbose_name='Опис')
    created_dt = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
    last_updated_dt=models.DateTimeField(verbose_name='Остання зміна', blank=True, null=True)
    order_status = models.TextField(verbose_name='Статус заявки', validators=[status_validator])
    

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)

















