# Generated by Django 4.2 on 2023-09-01 08:44

from django.db import migrations, models
import django.db.models.deletion
import orders_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField(verbose_name='Назва організації')),
                ('customer_address', models.TextField(verbose_name='Адреса')),
                ('customer_city', models.TextField(verbose_name='Місто')),
            ],
            options={
                'verbose_name': 'Опис контрагента',
                'verbose_name_plural': 'Опис контрагентів',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(verbose_name='Виробник')),
                ('model', models.TextField(verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Доступне обладнання ',
                'verbose_name_plural': 'Доступне обладнання',
                'db_table': 'devices',
            },
        ),
        migrations.CreateModel(
            name='DeviceInField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.TextField(verbose_name='Серійний номер')),
                ('owner_status', models.TextField(verbose_name='Статус власності ')),
                ('analyzer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.device', verbose_name='Ідентифікатор обладнання ')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.customer', verbose_name='Ідентифікатор користувача')),
            ],
            options={
                'verbose_name': 'Обладнання в полях',
                'verbose_name_plural': 'Обладнання в полях',
                'db_table': 'devices_in_fields',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_description', models.TextField(verbose_name='Опис')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('last_updated_dt', models.DateTimeField(blank=True, null=True, verbose_name='Остання зміна')),
                ('order_status', models.TextField(validators=[orders_app.models.status_validator], verbose_name='Статус заявки')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.customer', verbose_name='Кінцевий користувач')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.deviceinfield', verbose_name='Обладнання')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'db_table': 'orders',
            },
        ),
    ]